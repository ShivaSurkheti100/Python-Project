
# use of 'is'
a = None
if(a is None):  # here: "is" = " = = " ; mostly " == " is used
    print("Yes")
else:
    print("No")

print("")

# use of 'in' ; used in loop as well

a = [45, 56, 6, 9.0, 9]
print( 9.0 in a) # prints whether an item is present in the list or not
print(9 in a)
print(977 in a)

# Important note :
# There can be any number of elif statements
# else is executed only if all the conditions inside elif fails


