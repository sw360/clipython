# CLI Support for Python

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/sw360/clipython/blob/master/License.md)
[![Python Version](https://img.shields.io/badge/python-3.8%2C3.9-yellow?logo=python)](https://www.python.org/doc/versions/)
[![PyPI version](https://img.shields.io/badge/pypi%20package-1.2.1-green)](https://pypi.org/project/cli-support)
[![Static checks](https://github.com/sw360/clipython/actions/workflows/python-package.yml/badge.svg)](https://github.com/sw360/clipython/actions/workflows/python-package.yml)
[![Unit tests](https://github.com/sw360/clipython/actions/workflows/unit-test.yml/badge.svg)](https://github.com/sw360/clipython/actions/workflows/unit-test.yml)

Python library to read Component License Information (CLI) files. They can be
created by [FOSSology](https://www.fossology.org) and stored in
[SW360](https://www.eclipse.org/sw360/).

For more information about the CLI file format, please have a look at
[ComponentLicenseInformation.md](ComponentLicenseInformation.md).

## Usage

### Installation

This project is available as [Python package on PyPi.org](https://pypi.org/project/cli-support/).  
Install cli_support and required dependencies:

  ```shell
  pip install cli_support
  ```

### Required Packages

* none

## Using the API

* Start using the API:

  ```python
  import cli_support
  clifile = cli_support.CLI.CliFile()
  clifile.read_from_file("cli_filename")
  ```

## Contribute

* All contributions in form of bug reports, feature requests or merge requests are welcome!
* Please use proper [docstrings](https://realpython.com/documenting-python-code/) to document
  functions and classes.
* Extend the testsuite **poetry run pytest** with the new functions/classes

## Build

### Building Python package

For building the library, you need [Poetry](https://python-poetry.org/). Build is then
simply triggered using

```shell
poetry build
```

This creates the source and wheel files in ```dist/``` subdirectory -- which can then
be uploaded or installed locally using ```pip```.

## Test

Start the complete test suite or a specific test case (and generate coverage report):

```shell
poetry run pytest
```

or

```shell
poetry run coverage run -m pytest
poetry run coverage report -m --omit "*/site-packages/*.py"
poetry run coverage html --omit "*/site-packages/*.py"
```

## Demo

The script ``show_licenses.py`` shows how to use the library to retrieve some information
of a given CLI file.

```shell
python ./show_licenses.py ./test/testfiles/CLIXML_MIT_simple.xml
```

## License

The project is licensed under the MIT license.  
SPDX-License-Identifier: MIT
