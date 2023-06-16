## Find the factorial and no of trailing zeros in a factorial of a number in python


##::::::: Finding the factorial of number using what I learnt::::::::

##  5! = 120 : here, trailing zero is 1 
## 10! = 3628800; trailing zeros is 2

# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print(fact)

### :::::::::::::: Harry's coding logic ::::::::::::::::::::::::
### ::::: find factorial and trailing zeros in factorial for smaller number::::::

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1) # n! = (n-1)! ; recursive 

# def factorialTrailingZeros(num):
#     fac = factorial(num)
#     print(fac)
#     count = 0
#     while fac % 10 == 0:
#         count = count + 1
#         fac = fac/10
#     return count

# if __name__ == "__main__":
#     num = int(input("Enter a number:\n")) 
#     fac = factorial(num)
#     print(f"The factorial of {num} is {fac}")
#     print(factorialTrailingZeros(10))

## Calculating trailing zeros for bigger number:::bigger number ko factorial nikalda machine nai faatxa :::: but using below logic we can calculate the trailing zeros of bigger number

# 100! = 100//5 + 100//5*5
def factorialTrailingZeros(num):
    count = 0
    i = 5
    while (num//i >0): # or use (num//i != 0)
        count += int(num/i)
        i = i * 5
    return count

print(factorialTrailingZeros(10000))







