
'''
other dunder / magic methods in Python are:
__str__() --> used to set what gets displayed upon calling str(obj)

__len__() --> used to set what gets displayed upon calling len(obj)

'''


class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):  # dunder method
        return f"The number is {self.num}"

    def __len__(self):  # dunder method
        return 1


n = Number(9)
print(n)
print(len(n))

# research in Python doc as this is the main source
