
#multilevel inheritance ; child class becomes a parent for another child class
# methods  == functions 

# programmer ko hajurba person; programmer ko bau employee; employee ko bau person

class Person: 
    country = "India"
    name1 = "Muna"

    def takeBreath(self):          # this is method or function
        print("I am breathing....")
    
class Employee(Person): # Employee is child class
    company = "Honda"
    name2 = "Harry"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an Employee so I am luckily breathing...")
   
class Programmer(Employee): # Programmer is grand((nati) child class
    company = "Meta"
    
    def getSalary(self):
        print(f"No salary to programmers")

p = Person() # Person class ko object p vayo 
p.takeBreath()
# print(p.company) --> throws an error

e = Employee() # Employee class ko object e vayo
e.takeBreath()
print(e.company)

pr = Programmer() # Programmer class ko object pr vayo
pr.takeBreath() # latest wala(nearest parent ko  ) print garxa
pr.getSalary() # afnai class ko return ya print garxa
print(pr.name1) # access  Muna  from Person  class
print(pr.name2) # access  Harry from Employee class
print(pr.company) # afnai class ko return ya print garxa
print(pr.country) # access India from Person class













