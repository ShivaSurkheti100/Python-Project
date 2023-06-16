## Create a password generator using python--(use your thought machine)

## Method 1:

import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)

    pLen = int(input("Enter password length\n"))
    s = [] ## empty list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    print("Your password is: ")
    print("".join(s[0:pLen]))

## Method 2:

# import string
# import random

# if __name__ == "__main__":
#     s1 = string.ascii_lowercase
#     # print(s1)
#     s2 = string.ascii_uppercase
#     # print(s2)
#     s3 = string.digits
#     # print(s3)
#     s4 = string.punctuation
#     # print(s4)

#     pLen = int(input("Enter password length\n"))
#     s = [] ## empty list
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     s.extend(list(s4))
#     # print(s)
#     print("Your password is: ")
#     print("".join(random.sample(s, pLen)))


## usage of append and extend in list

# >>> a = [6, 5, 9, 1, 0]
# >>> b = [-7, 5, 4]
# >>> a.append(b)
# >>> a
# [6, 5, 9, 1, 0, [-7, 5, 4]]
# >>> a = [5, 4, 8, 9, -9]
# >>> b = [33, 44, 67]
# >>> a.extend(b)
# >>> a
# [5, 4, 8, 9, -9, 33, 44, 67]

# >>> a = "37949320123alkhfkafheiahflf"
# >>> list(a)
# ['3', '7', '9', '4', '9', '3', '2', '0', '1', '2', '3', 'a', 'l', 'k', 'h', 'f', 'k', 'a', 'f', 'h', 'e', 'i', 'a', 'h', 'f', 'l', 'f']





