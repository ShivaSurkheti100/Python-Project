letter = '''Dear <|NAME|>,
Greetings from ABC codiing house. I am happy to tell you about your selection
You are Selected !
Have a great day ahead!
Thanks and regards,
Date: <|DATE|>'''
name = input("Enter Your Name:\n")
date = input("Enter date:\n ")
letter = letter.replace("<|NAME|>", name) 
letter = letter.replace("<|DATE|>", date)
print(letter)