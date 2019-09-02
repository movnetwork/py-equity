#### PY-EQUITY

##### Installation
```shell script
$ pip install py-equity
```

##### Quick Usage
```python
from equity import Equity

# CONTRACT_PATH = "./LockWithPublicKey.equity"
CONTRACT_ARGS = [
    "e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78"
]

equity = Equity("http://localhost:9888")

equity = equity.compile_file(CONTRACT_PATH, CONTRACT_ARGS)

print(equity.json())

```

##### API

##### AUTHOR ~ MEHERET TESFAYE

##### LICENSE ~ AGPLv3+
