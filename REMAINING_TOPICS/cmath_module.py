'''cmath module is a built-in module that you can use for mathematical tasks for complex numbers.
The methods in this module accepts int, float, and complex numbers.
It even accepts Python objects that has a __complex__() or __float__() method.
The methods in this module almost always return a complex number.(except for constant)
If the return value can be expressed as a real number, the return value has an imaginary part of 0.'''

# cmath module has a set of methods and constants:
''' ::::::::cmath module::::::::::
cmath.sin(x)	    Returns the sine of x
cmath.sinh(x)	    Returns the hyperbolic sine of x
cmath.sqrt(x)	    Returns the square root of x
cmath.tan(x)	    Returns the tangent of x
cmath.tanh(x)	    Returns the hyperbolic tangent of x
cmath.phase()	    Return the phase of a complex number
cmath.polar()	    Convert a complex number to polar coordinates
cmath.acos(x)	    Returns the arc cosine value of x
cmath.acosh(x)	    Returns the hyperbolic arc cosine of x
cmath.asin(x)	    Returns the arc sine of x
cmath.asinh(x)	    Returns the hyperbolic arc sine of x
cmath.atan(x)	    Returns the arc tangent value of x
cmath.atanh(x)	    Returns the hyperbolic arctangent value of x
cmath.cos(x)	    Returns the cosine of x
cmath.cosh(x)	    Returns the hyperbolic cosine of x
cmath.exp(x)	    Returns the value of Ex, where E is Euler's number (approximately 2.718281...), and x is the number passed to it
cmath.isclose()	    Checks whether two values are close, or not
cmath.isfinite(x)	Checks whether x is a finite number
'''

import cmath
a = cmath.sqrt(9)
print(a) # returns the complex number with imaginary part 0

import cmath
b = cmath.asin(1)
print(b) # returns complex number with imaginary part 0

print(cmath.isfinite(0))
print(cmath.sin(cmath.pi/2))

'''cmath cosntants
cmath.e	    Returns Euler's number (2.7182...)
cmath.inf	Returns a floating-point positive infinity value
cmath.infj	Returns a complex infinity value
cmath.nan	Returns floating-point NaN (Not a Number) value
cmath.nanj	Returns coplext NaN (Not a Number) value
cmath.pi	Returns PI (3.1415...)
cmath.tau	Returns tau (6.2831...)

'''

import cmath
print(cmath.pi)
print(cmath.e) ## returns euler's number(2.7182.......)
print(cmath.tau)
