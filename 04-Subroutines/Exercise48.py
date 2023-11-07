def f(code):
    suma = int(code[0]) + int(code[1]) + int(code[2])
    if int(code[3]) == suma%7:
        return True
    else:
        return False
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))