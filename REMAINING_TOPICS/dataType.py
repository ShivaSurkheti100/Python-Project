'''Python has the following data types built-in datatypes by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType'''



a = "Hello World"	# str	
x = 20	# int	
x = 20.5	# float	

b = 1j	# complex	
x = ["apple", "banana", "cherry"] # list	
x = ("apple", "banana", "cherry") # tuple

c = range(6)	# range	
d = {"name" : "John", "age" : 36}	# dict	
e = {"apple", "banana", "cherry"}	# set	

x = frozenset({"apple", "banana", "cherry"})	#frozenset	

f = True	# bool	

x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	

y = None	# NoneType	

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(y)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(y))

## setting the specific data types:
# If you want to specify the data type, you can use the following constructor functions:

a = str("Hello World")	#str	

x = int(20)	#int
x = float(20.5)	#float

b = complex(1j)	#complex	

x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	

c = range(6)	#range	
d = dict(name="John", age=36)	#dict	
e = set(("apple", "banana", "cherry"))	#set	

x = frozenset(("apple", "banana", "cherry"))	#frozenset	

f = bool(5) #bool	

y = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(y)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(y))





