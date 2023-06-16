
#  function and methods; variable and atrribute(property) are interchangeable(same) in software world
''' 
# Without the use of static method
class Employee:
    def greet(self):
        print("Good Morning, Sir")

harry = Employee()
harry.greet()
Employee.greet(harry)

 '''

# Use of @staticmethod

class Employee:
    @staticmethod
    def greet(): # self haldo vane feri error aauxa 
        print("Good Morning, Sir")
    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee()
harry.greet()
harry.time()
Employee.greet()

# we can also pass other arguments besides 'self'

class Employee:
    company = "Facebook"
    def getSalary(self, greet):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{greet}")
   
harry = Employee()
harry.salary = 500000000
harry.getSalary("Thanks!") # greet ma "Thanks!"  argument pass vayo; self is passed automatically; 
