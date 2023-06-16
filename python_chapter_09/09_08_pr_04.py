
with open("sample2.txt") as f: # read mode ma
    content = f.read()

content = content.replace("donkey", "$%^@$^#")
with open("sample2.txt", "w") as f:
    f.write(content)
   
    


