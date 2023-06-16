# write a python program to make copy of this.txt file
# concept to create a new file is opening <new file> in write mode 
# and use f.write() method  to create a new file

with open("this.txt") as f:
    content = f.read()

with open("copy.txt", "w") as f:
    f.write(content)

    
