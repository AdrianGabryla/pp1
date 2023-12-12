def f(n):
    cards = {"A":10, "K":10, "Q":10, "J":10, "T":10}
    out = 0
    for i in n:
        if i.isdigit():
            out += int(i)
        else:
            out += cards[i]
    return out

if __name__=="__main__":
    print(f("2K9"))
    print(f("234AJ7"))