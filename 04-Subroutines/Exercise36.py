def f(detector):
    people = 0
    for i in detector:
        if i == "+":
            people += 1
        else:
            people -= 1
        if people == 3:
            return True
    return False
print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))