
# multiple inheritance ; child class inhertis more than one parent class

class Employee: # aama 
    company = "LinkedIn"
    eCode = 120

class Freelancer: # bau 
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1
        #print(self.level)

    
class Programmer(Freelancer, Employee): ## jun class paila lekheko xa teskai property or methods lai priority dinxa (print garda) 
    name = "Rohit" # Programmer ; child class ; xora/xori


p = Programmer() 
print(p.company)
print(p.level)
print(p.eCode)

p.upgradeLevel()
print(p.level) # use this or can use 14 th line code

## jun class paila lekheko xa teskai property or methods lai priority dinxa (print garda)
# e.g "LinkedIn" is printed as Employee class paila lekhya xa ni tw ....








