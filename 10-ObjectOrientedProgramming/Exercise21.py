class Statistics():
    def __init__(self):
        self.num = []
    def add(self, x):
        self.num.append(x)
    def show(self):
        out = ""
        for i in self.num:
            out = out + str(i) + " "
        return out
    def great(self):
        self.num.sort()
        return self.num[-1]
    def small(self):
        self.num.sort()
        return self.num[0]
    def mean(self):
        return sum(self.num)/len(self.num)
    def mediana(self):
        self.num.sort()
        if len(self.num)%2!=0:
            return self.num[int(len(self.num)/2)]
        else:
            return (self.num[int(len(self.num)/2)-1]+self.num[int(len(self.num)/2)])/2
x = Statistics()
x.add(12)
x.add(37)
x.add(6)
x.add(9)
x.add(17)
print(x.show())
print(x.great())
print(x.show())
print(x.small())
print(x.mean())
print(x.mediana())
x.add(24)
print(x.mediana())