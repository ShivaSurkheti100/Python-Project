
'''reduce syntax:
from functools import reduce
val = reduce(func, list1)
reduce applies a rolling computation to sequential pair of elements
sequential sum computation '''


from functools import reduce 
sum = lambda a, b: a + b
l = [1, 2, 3, 4, 5, 5]
val = reduce(sum, l)
print(val)
