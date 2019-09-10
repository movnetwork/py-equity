# py-equity

[![Build Status](https://travis-ci.org/meherett/py-equity.svg?branch=master)](https://travis-ci.org/meherett/py-equity)
![PyPI License](https://img.shields.io/pypi/l/py-equity.svg?color=black)
![PyPI Version](https://img.shields.io/pypi/v/py-equity.svg?color=blue)

*Python wrapper around the BUTXO Equity compiler for Bytom protocol.*

## Installation
```shell script
$ pip install py-equity
```

## Development
We welcome pull requests. To get started, just fork this repo, clone it locally, and run:
```
$ pip install -e . -r requirements.txt
```

## Quick Usage
```python
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

COMPILED = equity.compile_source(LOCK_WITH_PUBLIC_KEY_SOURCE,
                                 "e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78")

print(COMPILED["name"])
print(COMPILED["program"])
print(COMPILED["opcodes"])

print(COMPILED)

# Save compiled contract
equity.save()
```

`OUTPUT`

```json
"LockWithPublicKey"
"20e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e787403ae7cac00c0"
"0xe9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78 DEPTH 0xae7cac FALSE CHECKPREDICATE"

{"name": "LockWithPublicKey", "source": "\\n    contract LockWithPublicKey(publicKey: PublicKey) locks valueAmount of valueAsset {\\n      clause spend(sig: Signature) {\\n        verify checkTxSig(publicKey, sig)\\n        unlock valueAmount of valueAsset\\n      }\\n    }\\n", "program": "20e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e787403ae7cac00c0", "params": [{"name": "publicKey", "type": "PublicKey"}], "value": "valueAmount of valueAsset", "clause_info": [{"name": "spend", "params": [{"name": "sig", "type": "Signature"}], "values": [{"name": "", "asset": "valueAsset", "amount": "valueAmount"}]}], "opcodes": "0xe9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78 DEPTH 0xae7cac FALSE CHECKPREDICATE", "error": ""}
```

## CLI

Command line interface, run the following command:

```shell script
$ eqt --version
```

Example `eqt`:
```shell script
$ eqt --file LockWithPublicKey.equity --args "e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78"
```

Get help:
```shell script
$ eqt --help
```

From there, you can run eqt more commands, `-s\--save` to save your contract, `-u\--url` to change Bytom API url. by default (http://localhost:9888).

## Testing

You can run the tests with:

```
$ pytest tests
```

Or use `tox` to run the complete suite against the full set of build targets, or pytest to run specific 
tests against a specific version of Python.

## API

### Class Equity()

**Parameters**

`Optional`:
- `String` - *url*, Bytom API url, by default (http://localhost:9888).
- `String` - *api_key*, Bytom API key.
- `Integer` - *timeout*, request timeout, by default (1).

---

**`compile_source()`**: It is to compiling Bytom smart contract(Equity source).

**Parameters**

`Object`:
- `String` - *equity_source*, Equity source code.

`Optional`:
- `Boolean/String/Integer/Array` - **argv*.
    - `Boolean` - *boolean*, boolean parameter.
    - `String` - *string*, string parameter.
    - `Integer` - *integer*, integer parameter.

**Returns**

`Object`:
- `String` - *name*, contract name.
- `String` - *source*, contract source code.
- `String` - *program*, contract program.
- `Array` - *params*, contract params.
- `String` - *value*, contract value.
- `Array` - *clause_info*, contract clause_info.
- `Array` - *values*, contract values.
- `String` - *opcodes*, contract opcodes.
- `String` - *error*, contract error.

**Example**

```python
LOCK_WITH_PUBLIC_KEY_SOURCE = """
    contract LockWithPublicKey(publicKey: PublicKey) locks valueAmount of valueAsset {
      clause spend(sig: Signature) {
        verify checkTxSig(publicKey, sig)
        unlock valueAmount of valueAsset
      }
    }
"""
equity = Equity("http://localhost:9888", timeout=5)
COMPILED = equity.compile_source(LOCK_WITH_PUBLIC_KEY_SOURCE,
                                 "e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78")

print(COMPILED)
```
<details>
<summary>Output</summary>

```json5
{"name": "LockWithPublicKey", "source": "\\n    contract LockWithPublicKey(publicKey: PublicKey) locks valueAmount of valueAsset {\\n      clause spend(sig: Signature) {\\n        verify checkTxSig(publicKey, sig)\\n        unlock valueAmount of valueAsset\\n      }\\n    }\\n", "program": "20e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e787403ae7cac00c0", "params": [{"name": "publicKey", "type": "PublicKey"}], "value": "valueAmount of valueAsset", "clause_info": [{"name": "spend", "params": [{"name": "sig", "type": "Signature"}], "values": [{"name": "", "asset": "valueAsset", "amount": "valueAmount"}]}], "opcodes": "0xe9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78 DEPTH 0xae7cac FALSE CHECKPREDICATE", "error": ""}
```
</details>

----

**`compile_file()`**: It is to compiling Bytom smart contract form Equity file.

**Parameters**

`Object`:
- `String` - *equity_source*, Equity source code file(.equity or .eqt).

`Optional`:
- `Boolean/String/Integer/Array` - **argv*.
    - `Boolean` - *boolean*, boolean parameter.
    - `String` - *string*, string parameter.
    - `Integer` - *integer*, integer parameter.

**Returns**

`Object`:
- `String` - *name*, contract name.
- `String` - *source*, contract source code.
- `String` - *program*, contract program.
- `Array` - *params*, contract params.
- `String` - *value*, contract value.
- `Array` - *clause_info*, contract clause_info.
- `Array` - *values*, contract values.
- `String` - *opcodes*, contract opcodes.
- `String` - *error*, contract error.

**Example**

```python
LOCK_WITH_PUBLIC_KEY_PATH = "./LockWithPublicKey.equity"
equity = Equity("http://localhost:9888", timeout=5)
COMPILED = equity.compile_file(LOCK_WITH_PUBLIC_KEY_PATH,
                               "e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78")

print(COMPILED)
```
<details>
<summary>Output</summary>

```json5
{"name": "LockWithPublicKey", "source": "\\n    contract LockWithPublicKey(publicKey: PublicKey) locks valueAmount of valueAsset {\\n      clause spend(sig: Signature) {\\n        verify checkTxSig(publicKey, sig)\\n        unlock valueAmount of valueAsset\\n      }\\n    }\\n", "program": "20e9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e787403ae7cac00c0", "params": [{"name": "publicKey", "type": "PublicKey"}], "value": "valueAmount of valueAsset", "clause_info": [{"name": "spend", "params": [{"name": "sig", "type": "Signature"}], "values": [{"name": "", "asset": "valueAsset", "amount": "valueAmount"}]}], "opcodes": "0xe9108d3ca8049800727f6a3505b3a2710dc579405dde03c250f16d9a7e1e6e78 DEPTH 0xae7cac FALSE CHECKPREDICATE", "error": ""}
```
</details>

----

**`save()`**: Save compiled equity source.

**Parameters**

`Optional`:
- `String` - *file_path*, It is for full path with name.
- `String` - *dir_path*, It is for only dir path.

**Returns**

`Object`:
- `String` - *name*, contract name.

## AUTHOR
 [MEHERET TESFAYE](https://github.com/meherett)

## LICENSE
 [AGPLv3+](LICENSE)
