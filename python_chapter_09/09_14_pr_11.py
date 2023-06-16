# write a python program to rename a file to "removed_by_python.txt"

'''with open("shiva.txt") as f:
    s = f.read()

with open("removed_by_python.txt", "w") as f:
    f.write(s) 
the above syntax is used to copy file'''

# the below syntax is used to rename a file; i.e old file delete garerw new file create garxa
'''
import os 
with open("shiva.txt") as f:
    s = f.read()

with open("removed_by_python.txt", "w") as f:
    f.write(s)

os.remove("shiva.txt") # os.remove() method is used to remove or delete file

'''

# or use the below syntax ; same ho ; but learn in new way

import os

oldname = "shiva.txt"
newname = "renamed_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)


