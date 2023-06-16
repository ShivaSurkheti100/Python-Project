
def max(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3 # or use return num2
    else:
        if num2>num3:
            return num2
        else:
            return num3
m = max(55, 20, 99)
print("The maximum value is " + str(m))

