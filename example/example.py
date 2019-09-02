from equity import Equity

LOCK_WITH_PUBLIC_KEY_SOURCE = """
    contract LockWithPublicKey(publicKey: PublicKey) locks valueAmount of valueAsset {
      clause spend(sig: Signature) {
        verify checkTxSig(publicKey, sig)
        unlock valueAmount of valueAsset
      }
    }
"""

LOCK_WITH_PUBLIC_KEY_PATH = "./LockWithPublicKey.equity"
# LOCK_WITH_PUBLIC_KEY_ARGS = [
#     "e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78"
# ]

equity = Equity("http://localhost:9888")

equity = equity.compile_source(LOCK_WITH_PUBLIC_KEY_SOURCE,
                               "e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78")

print(equity["name"])
print(equity["program"])
print(equity["opcodes"])
