def greet(name): # fuction declaration
    print("Good Morning, " + name) # or use str(name) ; whatever you write under fuction ; that's function definition

greet("Shiva") # function call

''' types of function:
Built in function : print(), len(), sum(), range()
User defined function: defined by user; ex: greet(), percent()
'''
# functions with arguments
def greet(name):
    gr = "Hello " + name
    return gr 
a = greet("Harry")
print(a)
# or use this 
def greet(name):
    gr = "Hey " + name
    print(gr)

greet("Harry")
