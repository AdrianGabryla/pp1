class C():
    def __init__(self, arr):
        self.arr = arr
    def m(self, num):
        count = 0
        for i in self.arr:
            if i[0] > 0 and i[1] > 0:
                count += 1
        if count >= num:
            return True
        return False
    
x = C([[2,3],[1,8],[-6,4],[3,-7]])
print(x.m(2))
print(x.m(3))