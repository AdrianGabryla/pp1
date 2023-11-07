def f(num):
    t = True
    for i in num:
        if i == "0" or i == "1":
            t = True
        else:
            t = False
            break
    return t
print(f("1012100"))