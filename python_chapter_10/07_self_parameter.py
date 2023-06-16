
# self refers to the instance of class. It is automatically  passed with a function call from an object

'''
class Employee: 
    company = 'Google'
    def getSalary(self):
        print("Salary is 100k") # class attribute ko print garxa
        print(f"Salary is {self.salary}") # instance attribute ko print garxa
    
harry = Employee()
harry.salary = 100000 # instance attribute
# harry.company = 'Google' ; also can use instance varible instead of class varible ; you can refer in 06_instance_class_attribute.py
harry.getSalary()
# Employee.getSalary(harry) # or can use this for 11 th line ; don't use this ; ali sense banaudaina ; use 11 th line syntax

'''

class Employee:
    def getSalary(self): 
        print("Salary is 200k")
        print(f"Salary for this employee working in {self.company} is {self.salary}")


harry = Employee()
harry.company = "Google" # instance attribute
harry.salary = 1000000
harry.getSalary()

print("")

class Employee:
    company = "Google" # class attribute
    def getSalary(self): 
        print("Salary is 200k")
        print(f"Salary for this employee working in {self.company} is {self.salary}")


harry = Employee()
harry.salary = 1000000 
harry.getSalary()

# select garerw run garda error pani aauxa plus ; tempCodeRunnerFile.py pani create hunxa

