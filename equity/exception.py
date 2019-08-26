#!/usr/bin/env python
# coding=utf-8


class EquityAPIError(Exception):

    def __init__(self, status_code, error_message, error):
        self.status_code = status_code
        self.error_message = error_message
        self.error = error

    def __str__(self):
        return "(%s) %s" % (self.status_code, self.error)


class EquityClientError(Exception):
    def __init__(self, error_message, status_code=None):
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self):
        if self.status_code:
            return "(%s) %s" % (self.status_code, self.error_message)
        else:
            return self.error_message
