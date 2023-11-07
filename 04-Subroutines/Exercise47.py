def f(text):
    out=""
    for i in text:
        out = out + i + "-"
    return out[:-1]
print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))

