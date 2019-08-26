#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
from equity import *


def post_body(body):
    return json.dumps(body)


class Model(object):

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.data = json.dumps(dictionary)

    def object_from_dictionary(self):
        if self.dictionary == "" or self.dictionary == dict():
            return None

        return json.loads(self.data, object_hook=lambda d:
                          namedtuple('Object', d.keys())(*d.values()))

    def __repr__(self):
        return str(self)

    def __str__(self):
        if six.PY3:
            return self.__unicode__()
        else:
            return unicode(self).encode('utf-8')

    def __unicode__(self):
        return "APIModel"

    
class RPC(object):

    def __init__(self, api):
        self.api = api

    def get_base_path(self):
        return self.api.base_path

    def full_url(self, path):
        return "%s%s" % (self.api.url, path)

    def prepare(self, path, params):
        return self.full_url(path), post_body(params), dict()

    def create(self, url, body=None, headers=None):
        headers = headers or dict()
        if 'User-Agent' not in headers:
            headers.update({"User-Agent": "%s Python Client - %s" % (self.api.api_name, self.api.version)})
        if 'Content-Type' not in headers:
            headers.update({"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"})
        return requests.post(url, data=body, headers=headers, auth=self.api.auth)
