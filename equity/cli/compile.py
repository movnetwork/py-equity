#!/usr/bin/env python
# coding=utf-8

# IMPORT ALL PACKAGES
from equity import Equity


def _compile(url, equity_source, name, args=None, save=None):

    # Init Equity
    equity = Equity(url=url)

    # Compile equity source
    equity.compile_source(equity_source, args)

    if save:
        _, save_name = equity.save(dir_path=save)
    else:
        _, save_name = equity.save()

    print("Compiling is Done! %s" % save_name)

