
# create a class with a class attribute a ; create an object from it and set a directly using 
#  an object.a = 0. Does this change the class attribute ? 

class Sample:
    a = "Harry" # class attribute

obj = Sample()
obj.a = "Kohli" # instance attribute

# Sample.a = "Kohli" -->  but this is used to change class attribute

print(Sample.a) # this doesn't change class atrribute
print(obj.a)





