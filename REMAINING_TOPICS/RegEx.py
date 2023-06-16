''' RegEx or Regular Expression is a sequence of characters that forms a search pattern
RegEx can be used to check if a string contains the specified search pattern
Python has built-in package(module) called < re > to work with Regular Expressions'''


# check if string starts with "The" and ends with "Spain":

import re 
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Yes! We have a match")
else:
    print("No match")

## use of findall() function to return the list containing all matches
# print the list of all matches:
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

## returns an empty list if no matches were found
import re
txt = "The rain in Spain"
x = re.findall("Malta", txt) # returns []
print(x)

# search()fucn: searches the string for a match, and returns a match object if there is a match
# search for white-space character in the string
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

## if no matches were found, the value "None" is returned.
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt) # returns None
print(x)

## use of split()>> returns a list where the string has been split
# Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt) # \s-- whitespace character 
print(x)

#Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split(" ", txt, 1) # use " " or "\s" for white space character
print(x)

## use of sub()>> replaces the matches with the text of your choice:
# Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s","9", txt) # use " " or "\s" for white space character
print(x)

import re

#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) # use " " or "\s" for white space character
print(x)


''' Metacharacters are characters with a special meaning:::::
^	Starts with	                 "^hello"	
$	Ends with	                 "planet$"	
*	Zero or more occurrences	 "he.*o" 
'''


''' 
RegEx functions : re module offers a set of functions that allows us to search a string for a match:

findall     	Returns a list containing all matches
search	        Returns a Match object if there is a match anywhere in the string
split	        Returns a list where the string has been split at each match
sub	            Replaces one or many matches with a string

'''
