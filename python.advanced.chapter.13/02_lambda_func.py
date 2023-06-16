
# syntax: < func = lambda arguments: expression

# def func(a):
#     return a+5

# use above code or below that's the same

# func = lambda a:a+5

#### Use of Lambda function

func = lambda a:a+5
print(func(5))

square = lambda a : a**2 # or use a*a
print(square(6))

squareroot = lambda a:a**0.5
a = 16
print(squareroot(a))

cube = lambda a : a**3
print(cube(4))

sum = lambda a, b, c : a + b + c
x = sum(5, 6, 4)
print(x)

'''#this is what I understood 'bout func

def func(a):
    return a+5

x = func(5)
print(x)

# or use this 

def func(num):
    return num**2

print(func(7))

# or use this 

def func(num):
    print(f"The square root of {num} is {num**0.5}")
    
func(81) '''
