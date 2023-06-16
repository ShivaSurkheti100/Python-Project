# display the marks of 6 students in sorted manner i.e ordered sequence ma 
# input() le takes string as an input so ;also marks is integer ; so we do typecasting  
m1 = int(input("Enter Marks for Student Number 1: "))
m2 = int(input("Enter Marks for Student Number 2: "))
m3 = int(input("Enter Marks for Student Number 3: "))
m4 = int(input("Enter Marks for Student Number 4: "))
m5 = int(input("Enter Marks for Student Number 5: "))
m6 = int(input("Enter Marks for Student Number 6: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort() # list.sort() used to arrange data in ordered sequence
print(myList)





''' THIS IS WHAT CALLED TYPECASTING
a = input("enter number: ")
a = int(a)
print(a)
print(type(a)) '''