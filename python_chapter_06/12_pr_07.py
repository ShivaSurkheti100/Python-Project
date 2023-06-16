
# write a program to find out whether a given post is talking about "Harry" or not 
# I am using my own logic
post = '''Harry is an excellent coder . He is one of the best in the code game.
He teaches many Programming languages like Python, C , C++ , JavaScript, Java .'''

text = input("Enter the text to check:\n")

if(text in post):
    print("This post is talking about Harry.")
else:
    print("This post is not taling about Harry.")

# or use the program below

post = input("Enter the text:\n")
if("Harry" in post):
    flag = True
elif("coder" in post):
    flag = True
elif("Programming languages" in post):
    flag = True
else:
    flag = False
if(flag):
    print("This post is talking about Harry.")
else:
    print("This post is not talking about Harry.")

