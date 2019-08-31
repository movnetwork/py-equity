#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
from equity.utils import file_reader, file_writer, get_instance_name
from equity.exceptions import ConnectionError, Timeout, InvalidURL, ValueError, APIError
from equity.rpc import RPC
import requests

# Info
__NAME__ = "PY-Equity"
__VERSION__ = "0.1.0"
__AUTHOR__ = "Meheret Tesfaye"
__LICENSE__ = "AGPLv3+"

# Default bytom url
DEFAULT_URL = "http://localhost:9888"
TIMEOUT = 1


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
            self.timeout = TIMEOUT
        self._response = dict()
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

    def compile_file(self, file_path, args=None):
        if args is not None:
            if not isinstance(args, list):
                raise ValueError("Invalid instance of args! please use list instance.")
            else:
                _args = list()
                for arg in args:
                    instance_name = get_instance_name(arg)
                    _args.append({instance_name: arg})
        else:
            _args = list()
        equity_source = file_reader(file_path=file_path)
        _requests = dict(contract=equity_source, args=_args)
        rpc = RPC(self.url, self.api_key)
        compile_url = rpc.compile_url()
        _response = rpc.post(compile_url, _requests)
        self._response = _response.json()
        if "status" in self._response and self._response["status"] == "fail":
            raise APIError(self._response["msg"], self._response["error_detail"])
        elif "status" in self._response and self._response["status"] == "success":
            return self._response["data"]
        else:
            print(self._response)
            raise APIError("something is wrong", "please check your connection")

    def compile_source(self, equity_source, args=None):
        if args is not None:
            if not isinstance(args, list):
                raise ValueError("Invalid instance of args! please use list instance.")
            else:
                _args = list()
                for arg in args:
                    instance_name = get_instance_name(arg)
                    _args.append({instance_name: arg})
        else:
            _args = list()
        if not isinstance(equity_source, str):
            raise ValueError("Invalid instance of equity_source! please use only string(str) instance.")
        _requests = dict(contract=equity_source, args=_args)
        rpc = RPC(self.url, self.api_key)
        compile_url = rpc.compile_url()
        _response = rpc.post(compile_url, _requests)
        self._response = _response.json()
        if "status" in self._response and self._response["status"] == "fail":
            raise APIError(self._response["msg"], self._response["error_detail"])
        elif "status" in self._response and self._response["status"] == "success":
            return self._response["data"]
        else:
            print(self._response)
            raise APIError("something is wrong", "please check your connection")

    def save(self, file_path):
        return file_writer(file_path, self._response)

