def f(ex):
    a = int(ex[0])
    for i in range(len(ex)):
        if ex[i] == "+":
            a = a + int(ex[i+1])
        elif ex[i] == "-":
            a = a - int(ex[i+1])
    return a
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))