
# a match object is an object containing info about search and the result
# if there's no match, the value "None" will be returned, instead of match object

# Do a search that will return a Match Object:
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

# Print the position (start- and end-position) of the first match occurrence.
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # The regular expression looks for any words that starts with an upper case "S":
print(x.span())

# print the string passesd into the func 
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S"
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+",txt)
print(x.group())

# Note: If there is no match, the value < None > will be returned, instead of the Match Object.


'''The Match object has properties and methods used to retrieve information about the search, and the result:

.span()      returns a tuple containing the start-, and end positions of the match.
.string     returns the string passed into the function
.group()    returns the part of the string where there was a match

'''
