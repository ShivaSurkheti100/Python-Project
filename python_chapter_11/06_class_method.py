
''' class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    def changeSalary(self, sal):
        self.salary = sal #  or use self.sal = sal ; self instance attribute ko ho 
      

e = Employee()
print(e.salary) # prints 100
e.changeSalary(455)
print(e.salary) # prints 455
print(Employee.salary) # class atrribute Change vayena ; prints 100
'''
# Use of class attribute ; changes or adds class attribute
class Employee:
    company = "Neurolink"
    salary = 800
    location = "Dallas"

    @classmethod
    def changeSalary(cls, sal): # cls is used in the place of self
        cls.salary = sal
    
e = Employee()
#print(e.salary)
e.changeSalary(455)
#print(e.salary)
print(Employee.salary) # class attribute has been changed 


