# CLI for Python

Python library to read Component License Information (CLI) files.

# Usage

## Installation

### From Source

* Use directly this repository:
  
  ```shell
  pipenv install -e git+git@code.siemens.com/sw360/cli-python.git#egg=cli
  ```

### From BT-Artifactory

* using `pipenv`
  * ensure that your pipfile contains the correct source, i.e. something like
    ```
    [[source]]
    url = "https://devops.bt.siemens.com/artifactory/api/pypi/pypi-all/simple"
    verify_ssl = true
    name = "btartifactory"
    ```
  * run the following command
    ```shell
    pipenv install cli
    ```

* using `pip`:
  ```shell
  pip install cli
  ```

### Required Packages ##

* (none)

All dependencies can be installed using using `poetry` (*if you're not using [Poetry](https://python-poetry.org/), have a look at [pyproject.toml](pyproject.toml) for a list of dependencies*):
  
  ```shell
  poetry install
  ```

### Additional Steps

* Start using the API:

  ```python
  import cli
  clifile = cli.CLI.CliFile()
  ```

## Build

### Building Python package

For building the library, you need [Poetry](https://python-poetry.org/). Build is then simply triggered using

```shell
poetry build
```

This creates the source and wheel files in ```dist/``` subdirectory -- which can then be uploaded or installed locally using ```pip```.


## Demo ##

The script ``show_licenses.py`` shows how to use the library to retrieve some information of a given project on SW360.

## License
The project is licensed under the MIT license. SPDX-License-Identifier: MIT
