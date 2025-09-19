# `get-unicode-home`

A cross-platform utility to get the current HOME as a Unicode string.

## Features

- Works on both NT and POSIX.
    - Reads `HOME` on POSIX, `USERPROFILE`/`HOMEDRIVE`+`HOMEPATH` on Windows.
- Fully compatible with Python 2 and 3.

## Usage

```python
# coding=utf-8
from __future__ import print_function
from get_unicode_home import get_unicode_home

print(u'Detected HOME:', get_unicode_home())
```

## Installation

```bash
pip install get-unicode-home
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).