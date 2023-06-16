## least common multiple == lcm 
## This is Method 1:
# multiple of 6 = 6, 12, 18, 24, 30, 36, ....
# multiple of 8 = 8, 16, 24, 32, 40, 48, .....
# here : lcm = 24

### PseudoCode:
# 12, 8 : max = 12
# while(True):
#     if max%12 == 0 and max%8 == 0:
#         break
# max = lcm 

### METHOD 2: programatically
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

maxNum = max(a, b)

while(True):
    if maxNum%a == 0 and maxNum%b == 0:
        break
    else:
        maxNum += 1

print(f"The LCM of {a} and {b} is {maxNum}")


