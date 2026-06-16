# AGENTS.md

This file provides guidance to AI when working with code in this repository.

## Project Overview

Python library (`cli_support`) for reading and writing Component License Information (CLI)
XML files, used by FOSSology and SW360. Published on PyPI as `cli-support`.

## Build & Development

Uses [Poetry](https://python-poetry.org/) for dependency management and building.

```shell
poetry install          # install dependencies
poetry build            # build package to dist/
```

## Testing

```shell
poetry run pytest                          # run all tests
poetry run pytest tests/test_cli_clifile.py  # run a single test file
poetry run pytest -k "test_name"           # run a specific test

# with coverage
poetry run coverage run -m pytest
poetry run coverage report -m --omit "*/site-packages/*.py"
```

## Linting & Type Checking

- use type hints

```shell
poetry run flake8 .         # lint (CI checks E9,F63,F7,F82 as errors)
poetry run ruff check .     # ruff lint (E, F, UP, B, I rules; line-length 120)
poetry run isort .          # isort
mypy .                      # strict type checking (excludes /tests)
```

Mypy is configured in strict mode in pyproject.toml. The `/tests` directory is excluded from type checking.

## Naming Conventions

- Follow PEP 8 naming conventions
- Use ALL_CAPS for constants

## Code Quality

- Use meaningful variable and function names that clearly describe their purpose
- Include helpful comments for complex logic
- Add error handling for user inputs and API calls
- Use type hints throughout the codebase for better IDE support
- Include docstrings for all public methods

## Architecture

- `cli_support/CLI.py` — `CliFile`: top-level class that reads/writes CLI XML files. Entry point
  for the library.
- `cli_support/xml_base.py` — `XmlBase`: base class providing CDATA serialization and XML helpers.  
  Custom `_serialize_xml` is monkey-patched onto `xml.etree.ElementTree` in `CLI.py` to handle
  CDATA sections.
- `cli_support/cli_file_item_base.py` — shared base for items that have files/hashes (licenses,
  copyrights, etc.).
- Each CLI XML section maps to its own class: `CliLicense`, `CliCopyright`, `CliObligation`,
  `CliExportRestriction`, `CliExternalId`, `CliIrrelevantFiles`, `CliAssessmentSummary`, `CliGeneralInformation`.
- All section classes implement `_read_from_element()` and `_append_to_xml()` for XML round-tripping.
- `cli_support/license_tools.py` — `LicenseTools`: utility functions for license processing.
- Test XML fixtures live in `test/testfiles/`.
- `show_licenses.py` — demo script showing library usage.

## CI

Two GitHub Actions workflows run on push/PR:

- **Static checks**: flake8 + mypy across Python 3.8–3.11
- **Unit tests**: pytest + coverage across Python 3.8–3.11
