
names = ["harry", "shubham", "rohit", "rohan", 'aditi', '''shipra'''] # string declare garna ; can use; '' or "" or ''' '''
name = input("Enter the name to check: \n")

if(name in names):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")

print("The program is done !")
