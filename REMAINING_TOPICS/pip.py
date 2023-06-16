## PIP == package manager for python packages or modules

''' a package contains all the files you need for a module
Modules are python code libraries you can include in your project'''

# terminal : powershell : means : command line interface
## use < pip install pip > to install PIP 
## use < pip --version > to check if PIP is installed


## Download a package named "camelcase" usig < pip install camelcase >

## Then use the package after its installation :: it is used by importing the installed package(e.g camelcase)


import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
## this method capitalizes the first letter of each word


## Use the < pip uninstall camelcase > command to remove this package::::: Press <Y> and the package will be removed.

## use < pip list > or < pip freeze > to list all the packages installed on your system:



