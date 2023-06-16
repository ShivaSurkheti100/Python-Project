# There is no built-in function to reverse a String in Python.
# The fastest (and easiest?) way is to use a slice that steps backwards, -1.

# In this particular example, the slice statement [::-1] means start at the end of the string and
# end at position 0, move with the step -1, negative one, which means one step backwards.

txt = "Hello World"[::-1] ## slcicing the string 
print(txt)

'''If you like to have a function where you can send your strings,
and return them backwards, you can create a function and insert the code from the example above.'''

def my_func(x):
    return x[::-1] # slicing and returning the backward string
a = my_func("I wonder how this text looks like backwards.") # call the func with string as a parameter
print(a)

## [::-1] means slicing the string :: means starting at the end of string and moves backwards

