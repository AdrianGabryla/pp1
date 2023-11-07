def f(password):
    tab = []
    c = len(password)
    for i in password:
        tab.append(i)
    for j in range(len(password)):
        if password[j] in tab[j+1:]:
            c = c - 1
    if c >= 6:
        return True
    else:
        return False
print(f("ax15"))
print(f("boo123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))
