class C():
    def __init__(self, dic):
        self.dic = dic
    def m1(self, s, n):
        self.dic[s] = n
    def m2(self, s):
        out = 0
        for i in s:
            if i in self.dic:
                out += self.dic[i]
        return out
    
x = C({"A":120,"D":150,"G":90,"K":110})
x.m1("G",130)
print(x.m2("GD"))
print(x.m2("KEJ"))