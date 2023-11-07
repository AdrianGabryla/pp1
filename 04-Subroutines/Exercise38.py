def f(pal):
    for i in range(len(pal)):
        if pal[i-1] != pal[-i]:
            return False
    return True
print(f("radar"))