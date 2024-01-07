def f(n):
    n = str(n)
    tab = []
    for i in n:
        tab.append(int(i))
    x = list(filter(lambda y: (y%2!=0), tab))
    x.sort()
    if len(x) == 0:
        return -1
    else:
        return (x[-1]-x[0])
    
if __name__=="__main__":
    print(f(10852))
    print(f(7235973))
    print(f(4388))
    print(f(846206))