
## while comparing two values, python returns Boolean answer(True or False)

# print(10>=8)
# print(9<=9)
# print(5<2)
# print(7==7)
# print(9!=9)

## bool() function: gives you True or False in return:
## almost any value is evaluated to True  if it has some sort of content.

# print(bool(1)) ## any integers is True 
# print(bool("String")) ## any string is True 
# print(bool(7.9)) ## Any floating point numbers is True
# print(bool(True))
# print(bool(" ")) ## white space returns True

## Empty ones return False:

# print(bool("")) ## empty string -- returns False
# print(bool([]))  ## empty list returns False
# print(bool(())) ## empty tuple returns False
# print(bool({})) ## empty dictionary returns False
# print(bool(set())) ## empty set returns False
# print(bool(0)) ## zero returns False
# print(bool(None))  ## value "None" returns False
# print(bool(False)) # reutrns False

## you can type : (return 0) or (return False)

## Functions can return a Boolean

def myFunc():
    return True

print(myFunc())

print("")

## Python has built- in func that returns boolean value: i.e. -- isinstance()

x = 7.8 
print(isinstance(x, float)) # to check if an object is a float or not

y = 6
print(isinstance(y, int)) # to check if an object is an integer or not

z = 0
print(isinstance(z, float)) # to check if an object is a float or not

a = 'jgjgjg'
print(isinstance(a, str)) # to check if an object is a string or not

