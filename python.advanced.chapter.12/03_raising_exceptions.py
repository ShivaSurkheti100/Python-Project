# we can raise exceptions using <raise> keyword in python

## ValueError
def increment(num):
    try:
        return num + 1
    except:
        raise ValueError("This is not good -Harry")
a = increment("kkdfj747584kdfhskf") 
print(a) 

## ZeroDivisionError
# def increment(num):
#     try:
#         return num/0
#     except:
#         raise ZeroDivisionError("You are not allowed to divide any number by 0 !")

# c = increment(99)
# print(c) 



# # basic concept of functions plus exceptions handling(raising wala)
# def increment(num):
#     try:
#         print(num + 1)
#     except:
#         raise ValueError("This is not good -Harry")
# increment(9) 

# # or use this code
 
# def increment(num):
#     try:
#         return num + 1
#     except:
#         raise ValueError("This is not good -Harry")
# a = increment(755) 
# print(a) 
