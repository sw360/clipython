# CLI for Python

Python library to read Component License Information (CLI) files.

This is still **WORK-IN-PROGRESS.**

# Usage

## Installation

### From Source

* Use directly this repository:
  
  ```shell
  pipenv install -e git+git@code.siemens.com/sw360/cli-python.git#egg=cli
  ```

### From BT-Artifactory

* using `pipenv` does **not yet work**, sorry...

* using `pip`:
  ```shell
  pip install cli
  ```

### Additional Steps

* Start using the API:

  ```python
  import cli
  clifile = cli.CLI.CliFile()
  ```

## Demo ##

The script ``show_licenses.py`` shows how to use the library to retrieve some information of a given project on SW360.

