### This is my  own logic ; to print numbers divisible by 5
x = lambda a : a%5 == 0
l = [5, 22, 67, 85, 100, 3335, 2, 1]
print(list(filter(x, l)))

## Harry's logic 

l = [1, 2, 3, 5, 7, 10, 54, 1, 2, 3, 1, 5, 65, 90, 145]
a = filter(lambda a:a%5==0, l)
print(list(a))
