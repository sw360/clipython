# ------------------
# Run quality checks
# ------------------

# 2024-05-07, T. Graf

Write-Host "flake8 ..."
poetry run flake8

Write-Host "markdownlint ..."
npx -q markdownlint-cli *.md

Write-Host "isort ..."
poetry run isort .

Write-Host "mypy ..."
poetry run mypy .

Write-Host "Done."

# -----------------------------------
# -----------------------------------
