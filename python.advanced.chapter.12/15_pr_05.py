
num = int(input("Enter your number: "))
table = [i*num for i in range(1, 11)]
print(table)
with open("tables.txt", "a") as f:
    f.write(str(table))
    f.write("\n")



