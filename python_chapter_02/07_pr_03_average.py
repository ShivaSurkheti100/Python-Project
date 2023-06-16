'''a = input("Enter first number:")
b = input("Enter Second number:")
avg = (a+b)/2
print("The average of a and b is", avg)
THIS ONE IS WRONG CODE AS INPUT FUNCTION TAKES INPUT AS STRING 
OR READS INPUT AS STRING'''

a = input("Enter first number:")
b = input("Enter Second number:")
a = int(a) #typecasting is must as input() reads input as string
b = int(b)
avg = (a+b)/2
print("The average of a and b is", avg)