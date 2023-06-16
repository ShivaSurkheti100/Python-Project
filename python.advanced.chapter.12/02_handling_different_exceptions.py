

try:
    a = int(input("Enter a number: "))
    print(1/a)

except ValueError as e:  
    print("Please Enter a valid value!")
    print(e) 

except ZeroDivisionError as e: 
    print("Make sure you are not dividing by 0!") 
    print(e)
    
print("Thanks for using this code!") 


'''
simple program for try statement :

try:
    a = int(input("Enter a number: "))
    b = 1 / a
    print(b)

except Exception as e:
    print(e)
    
'''





























