
l = [1, 2, 99,  4, 58, 6, 70.99, 8, 9, 10]
for index, item in enumerate(l):
    if index == 2 or index == 4 or index == 6:
        print(f"The {index + 1}th element is {item}")
