from equity.utils import *
import pytest
import os


TRADE_OFFER_PATH = os.getcwd() + "/tests/TradeOffer.equity"

TRADE_OFFER_ARGS = [
    # assetRequested
    "1e074b22ed7ae8470c7ba5d8a7bc95e83431a753a17465e8673af68a82500c22",
    # amountRequested
    99,
    # seller
    "0014c5a5b563c4623018557fb299259542b8739f6bc2",
    # cancelKey
    "e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78"
]


def test_eqt(script_runner):
    eqt = script_runner.run('eqt', '--help')
    assert eqt.success
    
    
def test_cobra(script_runner):
    eqt = script_runner.run('eqt', '--version')
    assert eqt.success


# @pytest.mark.datafiles('/home/meheret/PycharmProjects/Cobra/tests/eqt.yaml')
# def test_compile(script_runner):
#     _compile = script_runner.run('eqt', '--file', TRADE_OFFER_PATH, "--args", TRADE_OFFER_ARGS)
#     assert _compile.success

