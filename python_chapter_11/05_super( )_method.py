# syntax; --< super().takeBreath() > as an example; super class(parent class)
# super() method or function is used to access the methods of a super class(parent class) in the child class
# super().__init__() calls the constructor of base class
''' class Person: 
    country = "India"

    def takeBreath(self):  # this is method or function
        print("I am breathing......................")
    
class Employee(Person): 
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath() # access methods of Person(parent) class
        print("I am an Employee so I am luckily breathing")
   
class Programmer(Employee): 
    company = "Meta"
    
    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()  # access methods of person and employee classes(parents); pailo yo run hunxa ani matra talako line; same in other case
        print("I am breathing ++++++++++++++++++++++")

p = Person() # Person object(p) banyo
p.takeBreath() # takeBreath() call gareko

e = Employee() # Employee object(e) banyo
e.takeBreath()

pr = Programmer() # Programmer object(e) banyo
pr.takeBreath()   '''

# super() method is used to run super(parent) class constructor ; __init__()
# yo talako problem fix vayena; i spent 1 hr on it. tarani vayena...fuck


class Person:

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breathing......................")


class Employee(Person):
    def __init__(self):
        super().__init__()  # yesle person class ko  __init__run garxa
        print("Initializing Employee...\n")

    def takeBreath(self):
        super().takeBreath()  # access methods of Person(parent) class
        print("I am an Employee so I am luckily breathing")


class Programming(Employee):
    def __init__(self):
        super().__init__()  # super().__init__()  --> prints Initializing Programmer only
        print("Initializing Programmer...\n")
    def takeBreath(self):
       super().takeBreath()  # access methods of person and employee classes(parents); pailo yo run hunxa ani matra talako line; same in other case
       print("I am breathing ++++++++++++++++++++++")


#p = Person()  # Person object(p) banyo
# p.takeBreath()  # takeBreath() call gareko

#e = Employee()  # Employee object(e) banyo
# e.takeBreath()

pr = Programming()  # Programmer object(pr) banyo
# pr.takeBreath()

