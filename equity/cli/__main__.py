#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
from equity.cli import *
from equity.utils import str2bool


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(
        prog="eqt",
        epilog=textwrap.dedent("""
                        !*! DONATION !*!
            Bytom (BTM): bm1qzx7pjr6whcaxmh9u0thkjuavf2ynk3zkgshhle
            """),
        description="Bytom smart contract, Equity language compiler."
    )

    parser.add_argument('--version', action='version',
                        version='Py-Equity version 0.1.0')

    parser.add_argument("-u", "--url", action="store", default="http://localhost:9888",
                        help="Bytom API url. Default(http://localhost:9888)")

    parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=True,
                        help="Equity smart contract source file.")

    parser.add_argument("-a", "--args", nargs="*",
                        help="Parameters of contract.")

    parser.add_argument("-s", "--save", action="store",
                        help="Save compiled bytom smart contracts.")

    try:
        _args = []
        parse_args = parser.parse_args()

        if parse_args.args is not None:
            args = parse_args.args
            for arg in args:
                try:
                    _args.append({"integer": int(arg)})
                except ValueError:
                    if str2bool(arg):
                        _args.append({"boolean": "true"})
                    elif str2bool(arg) is None:
                        _args.append({"string": arg})
                    else:
                        _args.append({"boolean": "false"})

        _compile(url=parse_args.url, equity_source=parse_args.file.read(),
                 name=parse_args.file.name, args=_args, save=parse_args.save)

    except Exception as exception:
        parser.error(str(exception))
