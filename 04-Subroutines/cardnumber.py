def f(num):
    out = ""
    out = num[:2] + 10*"*" + num[-4:]
    return out

if __name__ == "__main__":
    print(f("5290312400019022"))