
'''
# Use of @property:
class Employee:
    company = "Ncell"
    salary = 5600
    salarybonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()
print(e.totalSalary)
#print(e.totalSalary) # present it as property we use this syntax
# print(e.totalSalary()) // we can make a call but we wanna present it as proprety 
'''
 
# Use of @name.setter 
class Employee:
    company = "Ncell"
    salary = 5600
    salarybonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter  # beauty of python 
    def totalSalary(self, val):
        self.salarybonus = val - self.salary    # val = self.salary + self.salarybonus

e = Employee()
print(e.totalSalary)

e.totalSalary = 5800
print(e.salary) 
print(e.salarybonus)
