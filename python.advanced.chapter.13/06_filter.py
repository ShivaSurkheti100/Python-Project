
# filter syntax: list(filter(func, input_list)) ; can use lambda fucntion as well

def greater_than_5(num):
    if num > 5:
        return True  ## >5 ; vayeka sabai numbers print garxa
    else:
        return False

g10 = lambda num : num>10

l = [1, 2, 3, 4, 5, 6, 7, 89, 65, 45, 32, 21, 10, 16]
print(list(filter(greater_than_5, l)))
print(list(filter(g10, l)))

### we use lambda function for simple fucntion 