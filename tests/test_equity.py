from equity import Equity
import os

TRADE_OFFER_SOURCE = """
contract TradeOffer(assetRequested: Asset,
                    amountRequested: Amount,
                    seller: Program,
                    cancelKey: PublicKey) locks valueAmount of valueAsset {
  clause trade() {
    lock amountRequested of assetRequested with seller
    unlock valueAmount of valueAsset
  }
  clause cancel(sellerSig: Signature) {
    verify checkTxSig(cancelKey, sellerSig)
    unlock valueAmount of valueAsset
  }
}
"""

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


def test_source_and_path():

    equity = Equity("http://localhost:9888")

    COMPILED_FROM_SOURCE = equity.compile_source(TRADE_OFFER_SOURCE, TRADE_OFFER_ARGS)
    #
    COMPILED_FROM_PATH = equity.compile_file(TRADE_OFFER_PATH, TRADE_OFFER_ARGS)

    assert COMPILED_FROM_SOURCE["name"] == COMPILED_FROM_PATH["name"]

    assert COMPILED_FROM_SOURCE["program"] == COMPILED_FROM_PATH["program"]

    assert COMPILED_FROM_SOURCE["opcodes"] == COMPILED_FROM_PATH["opcodes"]

