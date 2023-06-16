

f = open("sample.txt")
#reads first line
text = f.readline() # reads one line from the file 
print(text)

#reads second line
text = f.readline() 
print(text)

#reads third line
text = f.readline() 
print(text)

#reads fourth line ....and so on...
text = f.readline() 
print(text)
f.close()
# gap aaunu ko karan; due to \n or new line character

'''Modes of Opening a file
r == open for reading
w == open for writing
a == open for appending  or adding data at the end of file
+ == opne for updating(both reading and writing

"rb" is used to open for reading in binary mode
"rt"(by default) or "r" is used to open for reading in text mode '''

