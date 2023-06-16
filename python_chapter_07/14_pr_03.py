# program to print multiplication table of a given number using while loop
# print("\n") is used to create two lines gap
# print(" ") is used to create one line gap 
n = int(input("Enter the number: "))
i = 1 # or count = 1
while i<=10:
    print(i*n)
    i = i + 1

# or use the program below

n = int(input("Enter the number: "))
i = 1 
while i<=10:
    print(str(n) + " X " + str(i) + " = " + str(n*i))
    i = i + 1


   











