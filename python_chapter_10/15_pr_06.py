
# these multi line codes are important concept! 
''' class Sample:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}")

obj = Sample("Harry")

print("**********") # or use print("")

# you can use this syntax as well

class Sample:
    def __init__(self, name):
        self.name = name 
    
obj = Sample("Harry")

print(obj.name)

 '''


# Can you change the self parameter inside a class to something else (say "harry") . Try changing self to "slf" or "harry" and set the effects
# the answer is justified by the following codes

# 'slf' can be used in the place of self.... 
# for understanding we can use slf, harry, shiva, math, ....anything in the place of self ; yini haru function kai parameter jastai hun

class Sample:
    def __init__(slf, name):
        slf.name = name 
    
obj = Sample("Harry")

print(obj.name)

print("**********")

# 'harry' can be used in the place of self

class Sample:
    def __init__(harry, name):
        harry.name = name 
    
obj = Sample("Harry")

print(obj.name)

print("**********")