# write a program to wipe out all the contents of a file using python

'''with open("myname.txt", "w") as f:
    f.write("In emceeing career, I have my name as GoatX.") 
# here I used f.write() to create myname.txt file
# I didn't create that file earlier ; I used f.write() method to create a new file'''

with open("myname.txt", "w") as f:
    f.write("") # blank string ; is used to wipe out all the contents

# or use this syntax
filename = "shiva.txt"
with open(filename, "w") as f:
    f.write("")


