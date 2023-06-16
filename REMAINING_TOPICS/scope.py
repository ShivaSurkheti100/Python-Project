## a variable is only available from inside the region it is created. this is called scope

## ::::::::Local scope:::::::can be used only inside the function
## a variable created inside a function is available inside that function
def myFunc():
    x = 990
    print(x)
myFunc()

## local varible can be accessed from a function inside(within) the function

def myFunc():
    x = 501
    def myInnerFunc():
        print(x)
    myInnerFunc()
myFunc()

## :::::Global Scope::::::a variable created in the main body of Python code is global varible and belongs to global scope
## Globla varibles are available from within any scope, global and local

## a variable created outside the function is global and can be used by anyone

x = 499 
def myfunc():
    print(x)
myfunc()
print(x)

'''If you operate with the same variable name inside and outside of a function,
Python will treat them as two separate variables, one available in the global scope (outside the function)
and one available in the local scope (inside the function):'''


## function will print local < x > then the code will print global < x >
x = 33.77  ## global scope(outside function)
def f():
    x = -99.87 ## local scope(inside function)
    print(x)
f()
print(x)

## global keyword: makes the variable global

# If you use global keyword , the variable belongs to global scope

def func():
    global x
    x = "GoatX"
func()
print(x)

# to change the value of global variable inside the func, refer to the variable using global keyword

x = "ShivaDaGoat"
def display():
    global x
    x = "GoatXonDaMic"
display()
print(x)

