#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
from equity import *


class Model(object):

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.data = json.dumps(dictionary)

    def object_from_dictionary(self):
        if self.dictionary == str() or self.dictionary == dict():
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
        return str("Model")
