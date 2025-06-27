# chk_input_form

`chk_input_form` is a Python utility that analyzes and classifies any given input into its data type and structure. It supports a wide range of values, including strings, numbers, booleans, None, NaN, complex numbers, and data containers like lists, tuples, and dictionaries.

## Features

- Detects input types: `str`, `int`, `float`, `complex`, `bool`, `NoneType`, `bytes`, `list`, etc.
- Recognizes and labels invalid or ambiguous inputs like `NaN`, `Infinity`, whitespace, and empty strings.
- Identifies numeric strings and evaluates expressions (e.g., `"2**2"` becomes `int:int`).
- Handles unusual inputs like memoryviews, frozensets, and bytearrays.
- Gracefully handles non-string data and classifies with `type:subtype` tags.

## Installation

```bash
pip install chk-input-form
```

## Usage

```python
from chk_input_form import chk_input_form

result = chk_input_form("  3.14  ")
print(result)  # str:float
```

Or try with other types:

```python
print(chk_input_form(123))           # int:int
print(chk_input_form(float('nan')))  # float:float-nan
print(chk_input_form([1, 2, 3]))     # list:list-3
```

## Authors

- Sajit Jose: <sajitjos@gmail.com>
- Jenfer Sajit: <jenifersajit@gmail.com>

## License

This project is licensed under the MIT License.
