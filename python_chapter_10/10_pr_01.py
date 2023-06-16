
# create a class programmer for storing information of few programmers working at microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name # object initialization using constructor
        self.prodcut = product 
    
    def getInfo(self):
        print(f"The name of {self.company} programmer is {self.name} and the product is {self.prodcut}")

amit = Programmer("Amit", "Skype")
shiva = Programmer("Shiva", "Insta")
harry = Programmer("Harry", "Github")
muna = Programmer("Muna", "DanceUp")

muna.getInfo()
amit.getInfo() # line lai jaa rakhyo tei sequence ma print hunxa
shiva.getInfo()
harry.getInfo()


