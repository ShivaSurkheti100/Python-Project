
marks = int(input("Enter the marks:\n"))

if(marks>=90):
    print("Your grade is Ex")
elif(marks>=80):
    print("Your grade is A")
elif(marks>=70):
    print("Your grade is B")
elif(marks>=60):
    print("Your grade is C")
elif(marks>=50):
    print("Your grade is D")  
else:
    print("Your grade is F")


# OR USE CONCATENATION OF STRINGS 


marks = int(input("Enter the marks:\n"))

if(marks>=90):
    grade = "Ex"  
elif(marks>=80):
    grade = "A"
elif(marks>=70):
    grade = "B"
elif(marks>=60):
    grade = "C"  
elif(marks>=50):
    grade = "D"
else:
    grade = "F"

print("Your grade is " + grade)

