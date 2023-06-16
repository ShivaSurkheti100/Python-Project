'''PROJECT_03 : STUDENT LIBRARY
Implement a student library system using oops where students can borrow a book 
from the list of books. 
Create a separate Library and Student class.
Your program must be menu driven.
You are free to choose methods and attributes of your choice to implement this functionality'''

class Library:
    def __init__(self, listOfBooks): # constructor
        self.books = listOfBooks 

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been issued to someone else. Please wait until the book is returned.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName) # return garepaxi tw thappinxa tw so add/append
        print("Thanks for returning this book! Hope you enjoyed reading it.")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Data Structure", "Python Notes", "Django", "Let us C"])
    centralLibrary.displayAvailableBooks()  ## centralLibrary is an object of Library class
    student = Student() # student object
    while(True):
        welcomeMsg = '''=====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))

        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()       
        else:
            print("Invalid Choice!")

   

