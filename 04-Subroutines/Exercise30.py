def f(number, even):
    out = 0
    if even:
        for i in str(number):
            if int(i)%2==0:
                out += int(i)
    else:
        for i in str(number):
            if int(i)%2!=0:
                out += int(i)
    return out
print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))
