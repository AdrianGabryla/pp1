import math
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        else:
            return 1
    def m2(self, a, b):
        if self.x >= 0 and a >= 0:
            if self.y >= 0 and b >= 0:
                return True
            if self.y <= 0 and b <= 0:
                return True
        elif self.x <= 0 and a <= 0:
            if self.y >= 0 and b >= 0:
                return True
            if self.y <= 0 and b <= 0:
                return True
        else:
            return False
    def m3(self, a, b):
        if math.sqrt((a-self.x)**2+(b-self.y)**2) > 5:
            return True
        else:
            return False

p = C(2,3)
print(p.m1())
print(p.m2(7,4))
print(p.m2(-3,1))
print(p.m3(8,5))
print(p.m3(4,7))
p1 = C(0,5)
print(p1.m1())
print(p1.m2(4,7))
print(p1.m2(-7,0))

        