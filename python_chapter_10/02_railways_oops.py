# oop is important cause we can model according to real world entity
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysapplication = RailwayForm() # harrysapplication is an object(new application); RailwayForm() is empty form
harrysapplication.name = "Harry" # form fill up
harrysapplication.train = "Rajdhani Express"
harrysapplication.printData() # runs the methods 
