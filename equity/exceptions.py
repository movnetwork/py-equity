#!/usr/bin/env python
# coding=utf-8


class APIError(Exception):

    def __init__(self, status_code, error_message, error):
        self.status_code = status_code
        self.error_message = error_message
        self.error = error

    def __str__(self):
        return "(%s) %s" % (self.status_code, self.error)


class ClientError(Exception):
    def __init__(self, error_message, status_code=None):
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self):
        if self.status_code:
            return "(%s) %s" % (self.status_code, self.error_message)
        else:
            return self.error_message


class ConnectionError(Exception):

    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return "%s" % self.error_message


class Timeout(Exception):

    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return "%s" % self.error_message


class InvalidURL(Exception):

    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return "%s" % self.error_message


class ValueError(Exception):

    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return "%s" % self.error_message


class NotFoundError(Exception):

    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return "%s" % self.error_message
