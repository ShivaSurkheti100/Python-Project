# with satement ; no need to use f.close()

with open("sample2.txt") as f:  # for read mode no need to use r
    a = f.read()
    print(a) 

with open("sample3.txt", "w")as f: # write mode ; it helps to create a new file ; file ma data can be updated
    f.write("What the fuck, you , motherfucking young ass !")





