# add static method in problem 2 to greet user with hello

 # Create a class calculator capable of finding square, cube and square root of a number

class Calculator:
    def __init__(self, num):
        self.num = num   # or can use self.number = num
    def square(self):
        print(f"The square of {self.num} is {self.num **2}")
    def cube(self):
        print(f"The cube of {self.num} is {self.num **3}")
    def squareRoot(self):
        print(f"The square root of {self.num} is {self.num **0.5}")
    
    @staticmethod
    def greet(): # @staticmethod ma self use hudaina
        print("*********Hello there welcome to the best calculator of the world**********")


number = Calculator(9) # or use this syntax; a = Calculator()
number.greet()
number.square()
number.cube()
number.squareRoot()
number.greet()




        
    


     