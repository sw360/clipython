# -----------------------------------------
# Run tests and create code coverage report
# -----------------------------------------

# 2022-03-09, T. Graf

poetry run coverage run -m pytest
poetry run coverage report -m --omit "*/site-packages/*.py"
poetry run coverage html --omit "*/site-packages/*.py"


# -----------------------------------
# -----------------------------------
