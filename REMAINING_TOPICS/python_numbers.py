
## three numeric types in Python are:  int(whole number, +ve, -ve), float(+ve, -ve, with decimals), complex(imaginary part: j) not "i"

x = -575757
y = 434739479347839830809999999999999999999999999999999203920

z = -5.0
z1 = 35e8 # 35 x 10^8
z2 = 12E4 # 12 x 10^4
z3 = -585.7e100

a = 3 + 5j
b = 0j
c = -88j
d = 55.57j
e = 53j

# print(type(x))
# print(type(y))
# print(type(z))
# print(type(z1))
# print(type(z2))
# print(type(z3))
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

## type conversions : you cannot convert complex numbers into another number type

x = 5
y = 9.0
z = 7j

a = complex(x)
b = int(y)
c = float(x)
d = complex(y)

# print(a)
# print(b)
# print(c)
# print(d)

# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1, 10)) ## displays a random number b/t 1 and 9
print(random.randint(1, 10))  ## displays a random number b/t 1 and 10




