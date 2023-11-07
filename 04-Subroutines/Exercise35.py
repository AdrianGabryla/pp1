def f(n1, n2, op):
    if op == "+":
        return n1+n2
    if op == "-":
        return n1-n2
    if op == "*":
        return n1*n2
    if op == "%":
        return n1%n2
    if op == "**":
        return n1**n2
print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))