# an attribute that belongs to instance(object) is called instance attribute
#  Employees ko name, age, salary different hunxa

class Employee:
    company = "Tesla"

harry = Employee()
rajni = Employee()
harry.salary = "50k"  #  this is instance variable 
rajni.salary = 30000  # adding instance attributes
print(harry.salary)
print(rajni.salary)


