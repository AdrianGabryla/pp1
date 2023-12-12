def f(e):
    out = int(e[0])
    for i in range(len(e)):
        if e[i] == "+":
            out += int(e[i+1])
        elif e[i] == "-":
            out -= int(e[i+1])
    return out

if __name__=="__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))