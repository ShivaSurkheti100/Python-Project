
# write a python function to remove a given word from a string and strip it at the same time
''' 
this = "                       Harry is a good boy "
print(this)
print(this.strip()) #  string.strip() ; removes spaces 
'''
def remove_and_strip(string, word):
    newStr = string.replace(word, "   ")
    return newStr.strip()

this = "          Harry is a good boy   "
n = remove_and_strip(this, "good")  # argument is passed ; string ma this; word ma Harry
print(n)


