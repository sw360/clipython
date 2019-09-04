from setuptools import setup, find_packages
 
setup(name='cli',
      version='1.0',
      license='SISL-1.2',
      author='Thomas Graf',
      author_email='thomas.graf@siemens.com',
      description='Support component license information (CLI) files',
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
      ],
      zip_safe=True)
