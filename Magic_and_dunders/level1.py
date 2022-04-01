from decimal import DivisionByZero
"""Practicle Application"""
class Vector:
    def __init__(self,x,y) -> None:
        self.x =x
        self.y= y
    def __add__(self,other_vec):
        return Vector(self.x + other_vec.x, self.y + other_vec.y)
    def __sub__(self,other_vec):
        return Vector(self.x - other_vec.x, self.y - other_vec.y)
    def __mul__(self,other_vec):
        return Vector(self.x * other_vec.x, self.y * other_vec.y)
    def __truediv__(self,other_vec):
        if other_vec.x <=0 or other_vec.y <= 0:
            raise DivisionByZero("Values contains zero")
        return Vector(self.x / other_vec.x, self.y / other_vec.y)
    def __repr__(self) -> str:
        return f"X:{self.x}  Y:{self.y}"
    def __len__(self):
        return 1
    def __call__(self, *args, **kwds):
        print("Got called")
    def __del__(self):
        print(f"Vector with value x:{self.x}, y:{self.y} is deleted")

if __name__=="__main__":
    v1 = Vector(1,10) #__init__
    v2 = Vector(2,20) #__init__
    v3 = v1+v2 #__add__
    print(v3) #__repr__ 
    print(v1-v2) #__sub__
    print(v1*v2) #__mul__
    print(v1/v2) #__truediv__
    print(len(v1)) #__len__
    v1() # __call__
    del v3 #__del__
    #__del__ for rest of the objects is deleted->FIFO
    