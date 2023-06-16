
# ## Using the module we just created(my_module) by using import statement

import my_module
a = my_module.greeting("GoatX!") ## func call
print(a)

import my_module
b = my_module.myDict["name"]
print(b)

## you can create an "alias" when you import a module, by using "as" keyword

import my_module as mx
c = mx.myDict["age"]
print(c)


