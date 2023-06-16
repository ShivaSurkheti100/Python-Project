### Use of f-string
# name = "Shiva Surkheti"
# marks = 99
# phoneNum = 9823830987
# print(f"This is me {name}")
# print(f"I obtained {marks} marks in maths")
# print(f"{phoneNum} is my contact number")

# print("")

# name = input("Enter the name: ")
# marks = int(input("Enter the obtained marks: "))
# phoneNum = int(input("Enter your phone number: "))
# print(f"This is me {name}.\nI obtained {marks} marks in maths\nAnd {phoneNum} is my contact number")

### Use of format method 

name = input("Enter the name: ")
marks = float(input("Enter the obtained marks: ")) # 99.5
phoneNum = int(input("Enter your phone number: "))
sentence = "This is me {}. I obtained {} marks in Science and {} is my contact number.".format(name, marks, phoneNum)
print(sentence)

#### yo chai harry ko code

# name = input("Enter the name: ")
# marks = input("Enter the obtained marks: ") # 99.5
# phoneNum = input("Enter your phone number: ")
# template = "The name of the student is {}, his marks is {} and phone number is {}"
# output = template.format(name, marks, phoneNum)
# print(output)
