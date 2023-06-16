
## finally clause ensures execution of code irrespective of exception


try:
    i = int(input("Enter a number: "))
    c = 1 / i

except Exception as e:
    print(e)
    exit()     # program exit huda poni executed hunxa 

finally:       # program exit huda poni executed hunxa 
    print("We are done!") # executed regardless of error

print("Thanks for using the program") # error aauda yo line run hunna feri due to exit()

# exit () use gareko vayerw 16th line run hudaina ; but finally clause ko code chai execute hunxa
