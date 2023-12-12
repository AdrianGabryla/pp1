def f(n):
    counter = 0
    for i in n:
        if i == "+":
            counter += 1
        else:
            counter -= 1
    return counter

if __name__=="__main__":
    print(f("+-+++-+---"))
    print(f("+-+++++-"))