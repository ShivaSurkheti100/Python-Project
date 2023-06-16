
# How to create an Indian Kirana Store calculator and receipts generator in basic python
'''write a python program which will keep adding a stream of numbers inputted by the user,
# The adding stops as soon as user presses q key on the keyboard'''

sum = 0
while (True):
    userInput = input("Enter the item price or press q to quit: ") # don't use int(input("....")) here 
    if userInput != "q":
        sum += int(userInput)
        print(f"Total order is {sum} so far.")
    else:
        print(f"Total bill amount is {sum}.Thank you for shopping with us! ")
        break

### Yo harry's ko code vayo 
# sum = 0
# while (True):
# 	userInput = input("Enter the item price or press q to quit: \n")
# 	if (userInput!='q'):
# 		sum = sum + int(userInput)
# 		print(f"Order total so far: {sum}")
# 	else:
# 		print(f"Your Bill total is {sum}. Thanks for shopping with us")
# 		break
