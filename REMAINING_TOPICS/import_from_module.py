
## import from module: can choose to import only parts from a module using "from" keyword


from my_module import myDict
a = myDict["age"]  # don't use modulename (mymodule.myDict["age"])
print(a)

from my_module import myDict
print(myDict["name"])

from my_module import greeting
print(greeting("Kiran!"))

## greeting() is returning None as well . Don't know why?