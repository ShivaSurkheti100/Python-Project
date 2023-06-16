
'''class Animals :
    animalType = "Domestic"

class Pets(Animals):
    color = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow bow!")

d = Dog()
d.bark() 
'''
# or use this is  multilevel inheritance 
class Animals :
    animalType = "Domestic"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")

d = Dog()
d.bark() 

