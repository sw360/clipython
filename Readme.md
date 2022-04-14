# CLI for Python

Python library to read Component License Information (CLI) files. They can be
created by [FOSSology](https://www.fossology.org) and stored in
[SW360](https://www.eclipse.org/sw360/).

For more information about the CLI file format, please have a look at
[ComponentLicenseInformation.md](ComponentLicenseInformation.md).

## Usage

### Installation

This project is available as [Python package on PyPi.org](https://pypi.org/project/cli-python/).  
Install cli and required dependencies:

  ```shell
  pip install cli
  ```

### Required Packages

* none

## Using the API

* Start using the API:

  ```python
  import cli
  clifile = cli.CLI.CliFile()
  ```

## Contribute

* All contributions in form of bug reports, feature requests or merge requests!
* Use proper [docstrings](https://realpython.com/documenting-python-code/) to document functions
  and classes
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
of a given project on SW360.

```shell
python ./show_licenses.py ./test/testfiles/CLIXML_MIT_simple.xml
```

## License

The project is licensed under the MIT license.  
SPDX-License-Identifier: MIT
