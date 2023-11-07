def f(binary_number):
    out = True
    for i in binary_number:
        if i == "1" or i == "0":
            out = True
        else:
            return False
    return out

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))