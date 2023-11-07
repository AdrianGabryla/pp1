def f(n):
    string = ""
    for i in range(n):
        string = string + ("*/") 
    return string[:-1]
print(f(4))
print(f(1))