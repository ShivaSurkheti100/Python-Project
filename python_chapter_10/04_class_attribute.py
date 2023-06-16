
class Employee:
    company = "Google" # specific to each class
# class attribute; sabai employess ko uii hunxa; like company
# instance attribute; e.g; employees ko name, age , salary different hunxa; 

harry = Employee() # object instantiation(object banaune)
rajni = Employee()
print(harry.company)
print(rajni.company)

Employee.company = "Youtube" # changing class attribute
print(harry.company)
print(rajni.company) 
 