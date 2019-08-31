#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
import requests
from equity.utils import post_body

# DEFAULT BYTOM API AND VERSION
DEFAULT_API_NAME = "Bytom"
DEFAULT_VERSION = "1.0.9"


class RPC(object):

    def __init__(self, url, auth=None, api_name=None, version=None):
        self.url = str(url)
        self.auth = tuple() if auth is None else tuple(auth)
        self.api_name = DEFAULT_API_NAME if not api_name else api_name
        self.version = DEFAULT_VERSION if not version else version

    def compile_url(self):
        if self.url.endswith("/"):
            return "%s%s" % (self.url, "compile")
        else:
            return "%s%s" % (self.url, "/compile")

    def check_header(self, headers):
        headers = headers or dict()
        if 'User-Agent' not in headers:
            headers.update({"User-Agent": "%s Python Client - %s" % (self.api_name, self.version)})
        if 'Content-Type' not in headers:
            headers.update({"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"})
        return headers

    def post(self, url, body=None, headers=None, timeout=1):
        body = post_body(body)
        headers = self.check_header(headers)
        return requests.post(url, data=body, headers=headers, auth=self.auth, timeout=timeout)

    def get(self, url, headers=None, timeout=1):
        headers = self.check_header(headers)
        return requests.get(url, headers=headers, auth=self.auth, timeout=timeout)
