
'''with open("log.txt") as f:
    content = f.read()

if "Python" in content:
    print("Yes python is present") 
Python and python is different thing in python ; as they are case sensitive
if statement matra use garda pani vo ; tara wrong statement huda ; kei print hunna 
so use else statment'''

with open("log.txt") as f:
    content = f.read()
if "python" in content:
    print("Yes, python is present")
else:
    print("No, python is not present")

# case sensitive hatauna
with open("log.txt") as f:
    content = f.read() # f.read().lower() or use
if "python" in content.lower(): # content.lower()
    print("Yes, python is present")
else:
    print("No, python is not present")

