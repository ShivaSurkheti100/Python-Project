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


number = Calculator(9) # or use this syntax; a = Calculator()
number.square()
number.cube()
number.squareRoot()



        
    


     