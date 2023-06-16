''' _ _ init _ _() is a special method which is first run as soon as the object is created
__int__() method  is also known as constructor. It takes <self argument> and can also take further arguments'''

''' ## use fo __init__() constructor
class Employee:
    company = "Google"
    def __init__(self): 
        print("Employee is created!")

harry = Employee() # harry is object  '''

class Employee:
    company = "Google"
    def __init__(self, name, salary, subunit):
        self.name = name  # object initialization by constructor 
        self.salary = salary  
        self.subunit = subunit
        print("Employee is created!")
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
       

    def getSalary(self): 
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee("Anderson", 700000, "YouTube")
#harry = Employee() --> throws an error as argument has to get passed; error(missing 3 required positonal arguments)
harry.getDetails() 

print("")

# simple program below  is my own practice another case

class Employee:
    def __init__(self,name, age, salary):
        self.name = "Shyam"
        self.age = "24 yrs" # yesto garda pani you have to pass arguments (line no. 49) 
        self.salary = 40000
        print("Employee is created!")

    def getInfo(self):
         print(f"The name of the employee is {self.name}")
         print(f"The age of the employee is {self.age}")
         print(f"The salary of the employee is {self.salary}")

harry = Employee("Shiva", "23 years old", 20000) # object can be instantiated using constructor liket this 
harry.getInfo()

        







