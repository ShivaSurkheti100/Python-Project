# In order to write to a file , we first open it in read or append mode
# then we use f.write() methods ; < writing > garda new file pani create hunxa
f = open("another.txt", "w")
f.write("Please write something in the file, regards ! ")
f.write(" and warm good morning ") # can be called multiple times
f.write("Please write something in the file, regards ! ")
f.write("and love and hugs to all of you ") # overwrite garda update garxa .txt file ma 
f.close() 

''' f = open("another.txt", "a") # append mode 
f.write(" I am appending") # adds data at the end of line 
f.close()

f = open("sample.txt", "a")
f.write("I am adding ") # jati program run garyo teti  ani <string> adds gardai janxa
f.close()   '''
