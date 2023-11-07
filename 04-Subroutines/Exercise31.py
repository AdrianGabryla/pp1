def f(x, y):
    num = 0
    for i in range(x, -1):
        i += 1
        if i%2==0:
            num += 1
    return num
print(f(-20, 11))