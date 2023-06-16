
# python function to print first n lines of star pattern for ; n = 3

n = 3
for i in range(n): # i starts from 0 to n-i
    print("*" * (n-i)) #  prints *  n-i times 

print(" ")

def star(n):
    for i in range(n):    # function definition
        print("*" * (n-i)) 

star(7) # function call 



 