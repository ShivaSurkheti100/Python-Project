## Binary method (strings)
# syntax : "and" .join(list) -- and ko thau ma can use any character

l = ["Camera", "Laptop", "Ipad", "Nvidia 3080 Graphic card"]
sentence = " and " .join(l)
print(sentence)

l = ["Camera", "Laptop", "Ipad", "Nvidia 3080 Graphic card"]
sentence = " , " .join(l)
print(sentence)

l = ("Camera", "Laptop", "Ipad", "Nvidia 3080 Graphic card")
sentence = "\t" .join(l)
print(sentence)

l = {"Camera", "Laptop", "Ipad", "Nvidia 3080 Graphic card"}
sentence = "\n" .join(l)
print(sentence)

print(type(sentence)) # class is "str"
# creates a string from iterable objects i.e can use list, tuple, set

