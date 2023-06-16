## iterator is an object that contains a countable no. of values
## list, tuple, dictionary, and set are iterable objects.

## returning an iterator from a tuple, and print each value:
myTuple = ("banana", "apple", "cherry")
myIter = iter(myTuple)
# print(myIter)
print(next(myIter)) #prints banana
print(next(myIter)) #prints apple
print(next(myIter)) #prints cherry

## Even strings are iterable objects and can return an iterator

myStr = "GoatX"
myIter = iter(myStr)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

# Looping through an iterator....using for loop to iterate through an iterable objects

myTuple = ('mango', 'guava', 'strawberry')
for fruit in myTuple:
    print(fruit)

# Create an Iterator

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

# The __next__() method also allows you to do operations, and must return the next item in the sequence.   






