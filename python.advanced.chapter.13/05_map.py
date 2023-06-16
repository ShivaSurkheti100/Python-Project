
## map syntax: < list(map(func, input_list)) > ; function can be lambda
## map applies a function to all the items in a list

#Method 2 : Using map 
l1 = [1,3, 4, 5, 7]
def square(num): 
    return num*num
print(list(map(square, l1))) # typecasting to list


## Method 1 : 

def square(num):
    return num**2
l = [1, 3, 4, 5, 7]
l2 = []   ## empty list
for item in l:
    l2.append(square(item))
print(l2)

