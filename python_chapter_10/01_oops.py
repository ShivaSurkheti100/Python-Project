
## DRY(DO NOT REPEAT YOURSELF) PRINCIPLE

## THE PROGRAM BELOW IS PROCEDURE ORIENTED PROGRAMMING
''' a = 32
b = 45
print("The sum of a and b is", 32 + 45)
print("The sum of a and b is", a + b)
print(f"The sum of {a} and {b} is {a + b}") # use of f-string
print(f"The sum of {a} and {b} is", a + b) '''

## THE PROGRAM BELOW IS OBJECT ORIENTED PROGRAMMING

class Number: # Number vanya class or template 
    def sum(self):                # class vitra ko part form vayo 
        return self.a + self.b

num = Number() #here num is an object; this is object instantiation i.e object ko instance; 
num.a = 12   # object instantiation which measn creating an object by giving a unique name 
num.b = 34
s = num.sum()
print(s)




# first ma class(template or form ) is made for giving an application (object)
# class means blueprint(template: i.e blank form) for creating objects (application of student after filling form)
# object is an executable file that can be run on computer
# class doesn't take memory; class contains info to create a valid object(application)
# class name is written in PascalCase
# i.e  class Employee:
#      ## methods & variables

''' 
PascalCase
e.g EmployeeName, ShivaSurkheti --> PascalCase

camelCase
e.g isNumeric, isFloat,isFloatOrInt,  shivaSurkheti --> camelCase

'''
