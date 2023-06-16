
a = 66 # global varibale
def func1():
    global a # global variable use garr vaneko ho
    print(f"Print Statement 1: {a}")

    a = 8 # local variable if global keyword is not used
    print(f"Print Statement 2: {a}")

func1() # function run  huna band hojayega
print(f"Print Statement 3: {a}") # a = 66 changed to a = 8 so, prints 8









# a = 54 # Global Varible
# def func1():
#     a = 8 # local variable
#     print(a)

# func1()
# print(a)