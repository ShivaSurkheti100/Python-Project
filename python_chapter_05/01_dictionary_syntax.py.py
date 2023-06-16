# key-value pair in dictionary corresponds to word-meaning

myDict = {
    "Fast": "In a quick manner",
    "Harry": "A coder", # string
    "Marks": [1, 2, 5], # list
    "decimal": (1.2, 2.5), # tuple
    "anotherdict": {"harry":"Player"} # dictionary vitra dictionary i.e nested dictinary
}
print(myDict)
print(myDict["Fast"]) # or print(myDict['Fast']) ; same
myDict["Marks"] = [45, 78]
print(myDict["Marks"])
print(myDict["decimal"])
print(myDict["anotherdict"]["harry"]) # nested dictionary(dict)

# dict is unordered ; means dict ko first key value ; fifth key value cannot be accessed; but list rw tuple ma milxa
# dict is mutable but tuple is unmutable; i.e. tuple ko values cannot be changed
# dict cannot contain duplicate keys i.e




