
## Built-in module

import platform
z = platform.system()
print(z) # prints windows

## Use of dir() function: used to list all the func names( or variable names) in a module
## dir() func can be used on all the modules, also the ones you create yourself

import platform
y = dir(platform)
print(y) 

## dir() prints in the form of "list"

