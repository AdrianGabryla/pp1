def f(t):
    import re
    num = re.findall('[0-9]+',t)
    out = 0
    for i in num:
        out += int(i)
    return out

if __name__=="__main__":
    print(f("11 and 4 is 15"))
    print(f("water12, and 3play is not 8"))