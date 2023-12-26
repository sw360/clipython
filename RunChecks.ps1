# ------------------
# Run quality checks
# ------------------

# 2023-12-24, T. Graf

poetry run flake8
npx -q markdownlint-cli *.md
poetry run isort .
poetry run mypy .


# -----------------------------------
# -----------------------------------
