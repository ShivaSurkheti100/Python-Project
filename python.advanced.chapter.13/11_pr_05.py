
# ## use of max function 
# print(max(6, 555, 9579, -888, 555, 1000))

from functools import reduce
l = [1,44, 64, 5, 6, 5, 49584, 8734, 873483, 384, 634]
a = reduce(max, l) ## don't call the function hai ...use directly
print(a)

### mechanism of program is: paila (1, 44) ma kun chai maximum xa herxa.
# feri (1, 44, 64) ma herxa . feri sequentially....(1, 44, 64, 5, 6, 5, 49584, 8734, 873483 herdai... 
# (1,44, 64, 5, 6, 5, 49584, 8734, 873483, 384, 634) ya pugxa ani finds the max number with the help
# of inbuilt function < max >
