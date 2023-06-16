''' create a python program to secure an existing password by replacing
a set of characters with the corresponding 'password-secure' character(provided as tuple): '''


SECURE = (("s", "$"), ("o", "0"), ("a", "@"), ("i", "1"), ("and", "&"))

def securePassword(password):
    for a, b in SECURE:
        password = password.replace(a, b)
    return password


if __name__ == "__main__":
    password = input("Enter your password:\n")
    password = securePassword(password)
    print(f"Your secured password is {password}")


