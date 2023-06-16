
# recursion is a function which calls itself
# n! = 1 * 2 * 3 * 4 * .... * n 
# n! = (n-1)! * n

# loop ko case ma :
n = int(input("Enter the number: "))
product = 1 # don't use this line inside for loop
for i in range(n):
    product = product * (i + 1) # i matra use garda ; resut = 0
    
print(product)

# function ko case ma :
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1) # don't use factorial
    return product 

print(factorial_iter(5))   
f = factorial_iter(5) # can directly use ; print(factorial_iter(5))
print(f) 

# recursion ko case ma
# factorial(n) = n x factorial(n-1)
def factorial_recur(n):
    if n == 1 or n == 0: # base condition
        return 1
    else:
        return n * factorial_recur(n-1) # function calling itself
f = factorial_recur(5)
print(f)


 




