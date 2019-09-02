#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
import json
from equity.exceptions import NotFoundError


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


def args(argv):
    _args = []
    if argv:
        _argvs = list(argv)
        for _argv in _argvs:
            if isinstance(_argv, list):
                for arg in _argv:
                    if isinstance(arg, dict):
                        _args.append(arg)
                    else:
                        instance_name = get_instance_name(arg)
                        if instance_name == "boolean" and arg:
                            _args.append({instance_name: "true"})
                        elif instance_name == "boolean" and not arg:
                            _args.append({instance_name: "false"})
                        else:
                            _args.append({instance_name: arg})
            else:
                instance_name = get_instance_name(_argv)
                if instance_name == "boolean" and _argv:
                    _args.append({instance_name: "true"})
                elif instance_name == "boolean" and not _argv:
                    _args.append({instance_name: "false"})
                else:
                    _args.append({instance_name: _argv})
    return _args


def file_reader(file_path):
    try:
        with open(file_path, 'r') as read_file:
            return_file = read_file.read()
            read_file.close()
        return return_file
    except FileNotFoundError:
        raise NotFoundError("Wrong file path, Please check your file path!")


def str2bool(v):
    if v.lower() in ("true", "True"):
        return True
    elif v.lower() in ("false", "False"):
        return False
    else:
        return None


def strip(_strip):
    return _strip.strip()[1:-1]


def post_body(body):
    return json.dumps(body)


def file_writer(file_path, body):
    try:
        with open(file_path, 'w') as write_file:
            write_file.write(body)
            write_file.close()
        return
    except FileNotFoundError:
        raise NotFoundError("Wrong file path, Please check your file path!")
