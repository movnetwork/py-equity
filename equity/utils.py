#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
import json


def get_instance_name(data):
    _type = type(data)
    if _type is str:
        return "string"
    elif _type is bool:
        return "boolean"
    elif _type is int:
        return "integer"
    else:
        return None


def file_reader(file_path):
    with open(file_path, 'r') as read_file:
        return_file = read_file.read()
        read_file.close()
    return return_file


def strip(_strip):
    return _strip.strip()[1:-1]


def post_body(body):
    return json.dumps(body)


def file_writer(file_path, body):
    with open(file_path, 'w') as write_file:
        write_file.write(body)
        write_file.close()
    return
