
name = "Harry"
print(name[0])
print(name[4])
# print(name[5]) doesn't return value as index starts from 0 to 4 i.e 0,1,2,3,4
# character of string cannot be changed but it can be accessed like above
# e.g name[3] = 'd' ->> doesn't work
#following program is slicing(tukra garne) of string
print(name[0:4]) # including first and excluding last i.e includes 0,1,2,3
print(name[1:3])
print(name[0:]) # sane as name[0:4] ; detect upto end
print(name[:4]) # same as name[0:4] ;detect from start
print(name[1:]) # same as name[1:5]
print(name[-5:-1]) # positive index starts from 0 to ...L to R
print(name[-3:-1]) # negative index starts from -1 to ..R to L
c = name[-4:-1] # same as name[1:4]
print(c)

# Slicing with skip value
name = "HarryIsGood" #  i.e. overwrite variable
d = name[0::2] #  2 means skips one character 
print(d)
d = name[0::3] #  3 means skips two character 
print(d)
# next e.g
mc = "GoatX"
e = mc[1:5:1]
print(e) # use 28th line or 29th line
print(mc[1:5:1])
e = mc[1:5:2]
print(e) # use 31st or 32nd line
print(mc[1:5:2]) 






























'''greeting = "Good Morning, "
name = "Harry"
print(greeting + name) # this is the addition of two strings
#print(type(name)) 
# or use this syntax
greeting = "Good Morning, "
name = "Harry"
c = greeting + name # Concatenating two strings or addition ....
print(c)
# array rw string ko index starts from 0 '''




