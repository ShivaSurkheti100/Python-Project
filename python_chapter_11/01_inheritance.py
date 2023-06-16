
# Inheritance is the way of creating a new class from an existing class.
# we can use the methods and attributes of Employee in Programmer class
''' syntax
class Employee     ## Base or PARENT CLASS = Employee
   #code
   
class Programmer(Employee):  ## derived or CHILD CLASS = Programmer
   #code  '''


''' class Employee:
   company = "Google"
   def whichCompany(self):
      print(f"The name of company is {self.company}")
   
   def showDetails(self):
      print("This is an employee")

class Programmer(Employee):
   language = "Python"

   def getLanguage(self):
      print("The language is {self.language}")

e = Employee()
# e.showDetails()
p = Programmer()
p.showDetails() #  here, Programmer class inherited everything from Employee class
p.whichCompany()
print(p.company)
So, use the above code to learn basic 'bout parent(base) and child(derived) class
 '''

# We can overwrite or add new attributes and methods in Programmer(child) class

class Employee:
   company = "Google"
   def showDetails(self):
      print("This is an employee")

class Programmer(Employee):
   language = "Python"
   company = "YouTube" # (#company = "YouTube"); class attribute overwrite garena vane Google nai print hanxa 

   def getLanguage(self):
      print(f"The language is {self.language}")

   def showDetails(self):
      print("This is a programmer")

e = Employee()
p = Programmer()
e.showDetails()
p.showDetails() # afnai(Programmer) class kai return garxa ; so yeslai nai vanxa Overwriting
print(p.company)

   


