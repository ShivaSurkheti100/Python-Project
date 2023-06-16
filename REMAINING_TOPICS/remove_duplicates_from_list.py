
## how to remove duplicates from a Python list
# Create a dictionary, using the List items as keys. 
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys.

myList = ["a", 'a', 'a', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'e']
myList = list(dict.fromkeys(myList))
print(myList)

'''If you like to have a function where you can send your lists, 
and get them back without duplicates, you can create a function and insert the code from the example above.'''

def my_function(x):
    return list(dict.fromkeys(x))
myList = my_function(['a', 'b', 'a', 'a', 'b', 'e', 'a', 'b'])
print(myList)

## creating dictionary and using list items as keys cause dictionary cannot have duplicate keys
## coverting the dictioanry into a list

