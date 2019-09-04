# --------------------------------------------
# Upload Python Packages 
# --------------------------------------------

# 2019-08-27, T. Graf

twine upload --verbose --repository-url https://devops.bt.siemens.com/artifactory/api/pypi/pypi-siemens dist\* -u $env:artifactory_user -p $env:artifactory_password
