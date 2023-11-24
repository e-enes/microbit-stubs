# microbit-stubs Python Library

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-v3.10%2B-blue.svg)](https://www.python.org/downloads/release)
[![Micro:bit Version](https://img.shields.io/badge/microbit-v2.2-blue.svg)](https://microbit.org/)

A Python library providing stubs for micro:bit modules, enabling code completion and static analysis in integrated development environments (IDEs).

## Overview

This library contains type hints (stubs) for the micro:bit modules, allowing developers to benefit from code completion, type checking, and static analysis in their Python projects that involve micro:bit programming. These stubs are compatible with popular Python IDEs like VSCode, PyCharm, and others.

## Features

- **Type Hints for micro:bit Modules**: Comprehensive type hints for various micro:bit modules, enhancing code readability and developer productivity.

- **IDE Compatibility**: Works seamlessly with major Python IDEs, providing an improved development experience for micro:bit projects.

- **Easy Integration**: Simply install the library using pip, and your IDE should automatically recognize and utilize the provided stubs.

## Installation

```bash
pip install microbit-stubs
```

## Usage

Once the library is installed, you can start using it in your micro:bit Python projects. Your IDE should automatically pick up the stubs and provide enhanced code completion and type checking.

```python
from microbit import *

# Now, your IDE should provide code completion for micro:bit modules.
display.show(Image.HAPPY)
sleep(1000)
display.clear()
```

## Contributing

We welcome contributions to enhance and expand the microbit-stubs library. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License 

This project is licensed under the MIT License - see the LICENSE file for details.

