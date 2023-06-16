# write a program for a list of words to be censored

words = ["fuck", "motherfucking", "young ass"]

with open("sample3.txt") as f:
    content = f.read()


for word in words: # like i in range()
    content = content.replace(word, "$@#&***")
    with open("sample3.txt", "w") as f:
        f.write(content)
