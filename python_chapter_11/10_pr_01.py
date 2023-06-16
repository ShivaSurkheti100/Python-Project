
# create a class c-2d vector and use it to create another class representing a 3-d vector

class C2dVec:

    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    

class C3dVec(C2dVec):
    
    def __init__(self, i, j, k):
        super().__init__(i, j) # use this in the place of -- self.icap <enter> self.jacap 
        self.kcap = k  

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(-8, 7)
v3d = C3dVec(1, 6, 3)

print(v2d)
print(v3d)







