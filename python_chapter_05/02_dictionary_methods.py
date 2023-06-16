# coding speed increase garna use lowercase
myDict = {
    "fast": "In a quick manner",
    "harry": "A Coder", # string
    "marks": [1, 2, 5], # list
    "decimal": (1.2, 2.5), # tuple
    1 : 2, # integer
    "anotherdict": {"harry":"Player"} # dictionary vitra dictionary i.e nested dictinary
}

# Dictionary Methods

# note : these commented items are imp codes

#print(myDict.keys()) # print the keys of dictionary
#print(type(myDict.keys())) # < class 'dict_keys'>
#print(list(myDict.keys())) # typecasting ; from dict_keys to list 

#print(myDict.values()) # prints the values of dictionary
#print(type(myDict.values())) # < class 'dict_values'>
#print(list(myDict.values())) # typecasting ; from dict_values to list
#print(tuple(myDict.values())) # typecasting ; from list to tuple

#print(myDict.items()) # returns the list of (key, value) tuples for all contents of dictionary

print(myDict)
print(" ") # maintains gap b\t lines
print(" ")
update_Dict = {
    "VTEN": "Real G",
    45: 88,
    "list": [66, 7.8, 10],
    "harry": "A Dancer"  # even mathi Coder thyo teslai change hanerw Dancer banaidinxa
}
myDict.update(update_Dict) # updates the dictionary by adding key-value pairs from updateDict
print(myDict)

# myDict.get()
print(myDict["harry"]) # prints value associated with key "harry"
print(myDict.get("harry")) # prints value associated with key "harry"
# 39 th rw 40 th line le same kaam garxa so why do we need myDict.get() ?

# so this is the difference between .get and [] syntax in Dictionaries
print(myDict.get("harry2"))  # Returns NONE as harry2 is not present in the dictionary
print(myDict["harry2"])      # throws an error as harry2 is not present in the dictionary








