#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
from equity.utils import file_reader, file_writer, get_instance_name, args
from equity.exceptions import ConnectionError, Timeout, InvalidURL, ValueError, APIError, NotFoundError
from equity.rpc import RPC

import requests
import os
import json

# Info
__NAME__ = "PY-Equity"
__VERSION__ = "0.1.0"
__AUTHOR__ = "Meheret Tesfaye"
__LICENSE__ = "AGPLv3+"

# Default bytom url and timeout
DEFAULT_URL = "http://localhost:9888"
DEFAULT_TIMEOUT = 1


class Equity(object):

    def __init__(self, url=None, api_key=None, timeout=None):
        self.url = DEFAULT_URL if not url else url
        if api_key and isinstance(api_key, str):
            self.api_key = str(api_key).split(":")
        else:
            self.api_key = str()
        if timeout and isinstance(timeout, int):
            self.timeout = int(timeout)
        else:
            self.timeout = DEFAULT_TIMEOUT
        self._response = dict()
        self.save_name = str()
        self._check_url(self.url)

    def _check_url(self, url):
        try:
            return requests.get(url, timeout=self.timeout)
        except requests.exceptions.InvalidURL:
            raise InvalidURL("Wrong url, Please check your's url(%s)!" % url)
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Please check your's internet connection or your's url(%s)!" % url)
        except requests.exceptions.Timeout:
            raise Timeout("Timeout error url(%s)!" % url)
        except Exception:
            raise ConnectionError("Something is wrong url(%s)!" % url)

    def is_working(self, url=None):
        try:
            if url and isinstance(url, str):
                return True if requests.get(url, timeout=1).status_code == 200 else False
            else:
                return True if requests.get(self.url, timeout=1).status_code == 200 else False
        except Exception:
            return False

    def compile_file(self, file_path, *argv):
        if not os.path.isfile(file_path) or not isinstance(file_path, str):
            raise NotFoundError("No such file: %s!" % file_path)
        if str(file_path).endswith(".equity"):
            self.save_name = os.path.basename(file_path)[:-7] + ".json"
        elif str(file_path).endswith(".eqt"):
            self.save_name = os.path.basename(file_path)[:-4] + ".json"
        else:
            self.save_name = os.path.basename(file_path) + ".json"
        equity_source = file_reader(file_path=file_path)
        _args = args(argv)
        _requests = dict(contract=equity_source, args=_args)
        rpc = RPC(self.url, self.api_key)
        compile_url = rpc.compile_url()
        _response = rpc.post(compile_url, _requests, timeout=self.timeout)
        self._response = _response.json()
        if "status" in self._response and self._response["status"] == "fail":
            if self._response["msg"] and "detail" in self._response:
                raise APIError(self._response["msg"], self._response["detail"])
            elif self._response["msg"] and "error_detail" in self._response:
                raise APIError(self._response["msg"], self._response["error_detail"])
            else:
                raise APIError("something is wrong", "please check your source!")
        elif "status" in self._response and self._response["status"] == "success":
            self.save_name = self._response["data"]["name"] + ".json"
            return self._response["data"]
        else:
            print(self._response)
            raise APIError("something is wrong", "please check your connection")

    def compile_source(self, equity_source, *argv):
        _args = args(argv)
        if not isinstance(equity_source, str):
            raise ValueError("Invalid instance of equity_source! please use only string(str) instance.")
        _requests = dict(contract=equity_source, args=_args)
        rpc = RPC(self.url, self.api_key)
        compile_url = rpc.compile_url()
        _response = rpc.post(compile_url, _requests, timeout=self.timeout)
        self._response = _response.json()
        if "status" in self._response and self._response["status"] == "fail":
            if self._response["msg"] and "detail" in self._response:
                raise APIError(self._response["msg"], self._response["detail"])
            elif self._response["msg"] and "error_detail" in self._response:
                raise APIError(self._response["msg"], self._response["error_detail"])
            else:
                raise APIError("something is wrong", "please check your source!")
        elif "status" in self._response and self._response["status"] == "success":
            self.save_name = self._response["data"]["name"] + ".json"
            return self._response["data"]
        else:
            raise APIError("something is wrong", "please check your connection")

    def save(self, file_path=None, dir_path=None):
        _compiled_ = json.dumps(self._response["data"], indent=4)
        if file_path:
            return file_writer(file_path, str(_compiled_)), self.save_name
        elif dir_path:
            if os.path.isdir(dir_path):
                return file_writer(os.path.join(dir_path, self.save_name), str(_compiled_)), self.save_name
            else:
                raise NotFoundError("Not found this directory: %s" % dir_path)
        else:
            return file_writer(self.save_name, str(_compiled_)), self.save_name

