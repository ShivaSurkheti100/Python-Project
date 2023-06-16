
# special methods ; add and  multipy are given in Python Documentation
# Operators in Python can be overloaded using dunder methods 
# These methods are called when 'a given ooperator' is used on the 'objects'

class Number :
    def __init__(self, num):
        self.num = num 
    
    def __add__(self, num2): # use add to overload '+'
       print("Let's add")
       return self.num + num2.num
    
    def __sub__(self, num2):
        print("Let's subtract") # use sub to overload "-"
        return self.num - num2.num
    
    def __mul__(self, num2): # use mul to overload '*'
        print("Let's multiply")
        return self.num * num2.num
    
    def __truediv__(self, num2): # use truediv to overload '/'
        print("Let's do true division")
        return self.num / num2.num 
 
    def __floordiv__(self, num2): # use floordiv to overload '//'
        print("Let's do floor division")
        return self.num // num2.num
        
    def __pow__(self, num2):
        print("Let's find out the power of number:")
        return pow(self.num, num2.num)   ## use pow to overload ....

n1 = Number(6) # n1 is Number object not an integer 
n2 = Number(6)

sum = n1 +  n2
print(sum)

sub = n1 - n2
print(sub)

mul = n1 * n2
print(mul)

truediv = n1 / n2
print(truediv)

floordiv = n1 // n2 
print(floordiv)

power = pow(n1, n2)
print(power)










