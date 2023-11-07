def f(x,y):
    a=0
    for i in range(x,y+1):
        if i%2==0 and i%3==0 and i%4!=0:
            a = a + i
    return a
print(f(1,20))
print(f(10,30))