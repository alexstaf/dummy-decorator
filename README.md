# dummy-decorator: A simple python decorator that does nothing

If you need to make a logic when some useful decorator is optional, you can use this dummy decorator to replace it when needed.

## Installation

Use the following command to install the package:

```bash
pip install dummy-decorator
```

## Usage example

```py
from dummy_decorator import dummy_decorator

@dummy_decorator
def function():
    ...
```
