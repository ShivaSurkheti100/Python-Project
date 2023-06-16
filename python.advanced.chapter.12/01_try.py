
#exception means an error that occurs during the execution of program
#exception(error) handling in Python 

''' exceptions can be handled using try statement
syntax is;

try:
    #code --> code which might throw an error
except Exception as e:
    print e
when exception is handled , the code flow continues without program interruption'''


'''
# this is general case of exception handling
try:
    a = int(input("Enter a number: "))
    print(1/a)

except Exception as e: # this is exception/error handling
    print("Exception occured!")
    print(e) # error lai print gareko hoina 
    
print("Thanks for using this code!") '''

# another example:
while(True):
    a = input("Enter a number: ")
    print("press q to quit")

    if a == "q":
        break

    try:
        print("Trying....")
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")
