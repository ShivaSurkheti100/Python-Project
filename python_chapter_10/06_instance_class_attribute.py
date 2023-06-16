

# instance attribute takes preference over class attribute during assignment and retrieval
class Employee:
    company = "Tesla"
    salary = 1000 # this is class variable

harry = Employee()
rajni = Employee()
# creating instance attribute salary for both objects
#harry.salary = "50k"  #  this is instance variable 
#rajni.salary = 30000
harry.salary = 45 # this is new instance varible
print(harry.salary)
print(rajni.salary) # adding instance attributes / variable

# below line throws an error as address is not present in instance/class
# print(rajni.address) 

'''
harry.attribute1 
1: Is attribute1 present in object ?
2: Is attribute1 present in class ?
preference order of printing first; instance attribute > class attribute 
'''