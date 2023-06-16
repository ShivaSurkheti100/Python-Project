# write a python function to print multiplication table of a given number

def multiply(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {i*num}") # use of f-string 

multiply(10)

print(" ")

def multiply(num):
    for i in range(1, 11):
        print(i*num) 

multiply(10)
