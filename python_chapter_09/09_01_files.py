
# RAM is volatile and all its contents are lost once a program terminates.
# in order to persist data forever, we use files
# a file is a data stored in a storage device. A python program can talk to the file by reading content from it and wriiting content to it
# open(filename, r) buit-in  funtion is used to open file 
# open("sample.txt", "r") ; r == opening mode

# use open function to read the content of a file

f = open("sample.txt")  # or use open("sample.txt", "r") ; by default the mode is r
text = f.read()  #  also can use open('sample.txt','r') or open("sample.txt")
print(text)
f.close()   

f = open("sample.txt", "rt") # "rt" by default // "r" by defalult // simply don't use rt/r
text = f.read(7) # reads first 6 characters from the file
print(text)
f.close()








