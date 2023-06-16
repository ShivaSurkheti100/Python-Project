# write a program to find out whether a file is identical and matches the content of another file

file1 = "copy.txt"
file2 = "this.txt"

with open(file1) as f:
    f1 = f.read()

with open("this.txt") as f: # can use(file2); cause it is defined already
    f2 = f.read()
if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")


# f1 and f2 ; duita files ko lagi use two different variables

file1 = "copy.txt"
file2 = "log.txt"

with open(file1) as f:
    f1 = f.read()

with open("log.txt") as f: # can use(file2); cause it is defined already
    f2 = f.read()
if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")