#  hcf = highest common factor : 9, 18 ma hcf = 9 : {28, 12} ma hcf = 4: hcf =1 (compulsory)
## hcf vanya the highest number which divides the both numbers

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))

if num1<num2:
    min = num1
else:
    min = num2

for i in range(1, min+1):  ### two numbers are m, n and min = m
    if num1%i == 0 and num2%i ==0:
        hcf = i
        
print(f"The HCF/GCD of two numbers is {hcf}")


    





































