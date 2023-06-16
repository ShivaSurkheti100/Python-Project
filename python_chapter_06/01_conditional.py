# tab = 4 spaces = indentation ; giving spaces
# elif means else..if
##if-elif-else ladder in Python

#a = 8
#if(a<3):
#    print("The value of a is greater than 3")
#elif(a>13):
#    print("The value of a is greater than 13")
#elif(a>7):
#    print("The value of a is greater than 7")
#elif(a>17):
#    print("The value of a is greater than 17")
#else:
#    print("The value of a is not greater than 3 or 7")

#print("Done!")

## Multiple if statements in Python ; first 3 if statements are independent entity; if-else chai ladder vayo 
a= 8
if(a<3): # independent statement ; executes if it is true
    print("The value of a is greater than 3")

if(a>13): # independent statement ; executes if it is true
    print("The value of a is greater than 13")

if(a>7): # independent statement ; executes if it is true
    print("The value of a is greater than 7")

if(a>17): # this is if-else ladder; yo xuttai ho feri; executes if() if its true ; natra else statement execute hunxa
        print("The value of a is greater than 17")
else:
    print("The value of a is not greater than 3 or 7")