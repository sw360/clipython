# CLI for Python

Python library to read Component License Information (CLI) files

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
  import sw360
  client = sw360.SW360(sw360_url, sw360_api_token)
  ```

## Demo ##

The script ``check_project.py`` shows hot to use the library to retrieve some information of a given project on SW360.

