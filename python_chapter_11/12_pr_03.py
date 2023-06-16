
# salaryAfterIncrement(sai)= salary * increment

class Employee:
    salary = 1000
    increment = 2.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai  / self.salary

e = Employee()
print(e.salaryAfterIncrement) # property use gareko xA
print(e.increment)

e.salaryAfterIncrement = 5500
print(e.increment)
