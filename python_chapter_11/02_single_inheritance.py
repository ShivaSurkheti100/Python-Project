# single inheritance ; child class inherits only a single parent class.
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
