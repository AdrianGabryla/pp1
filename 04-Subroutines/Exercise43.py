def f(name):
    out=""+name[0]
    for i in range(len(name)):
        if name[i] == " ":
            out = out + name[i+1]
    return out
print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))