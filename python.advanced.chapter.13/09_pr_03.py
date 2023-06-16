
## A list contains the multiplication table of 7 . write a program to convert it to a vertical string of same numbers

# # used my own brain to print table of certain number
# num = 8
# table = [i*num for i in range(1, 11)]  ## i starts from 1 to 10
# print(table)

### solution of problem no.3
l = [str(7*i) for i in range(1, 11)]  # typecasting chaixa rey ; cause; < .join(list) > joins strings
verticalTable = "\n".join(l)
print(verticalTable)


