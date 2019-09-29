# -------------------------------
# Build Packages for distribution
# -------------------------------

# 2019-09-29, T. Graf

python setup.py sdist
python setup.py bdist
python setup.py bdist_wheel
