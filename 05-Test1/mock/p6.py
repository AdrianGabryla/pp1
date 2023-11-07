def f(number, even):
    suma = 0
    num = str(number)
    if even:
        for i in num:
            if int(i)%2==0:
                suma += int(i)
    else:
        for i in num:
            if int(i)%2!=0:
                suma += int(i)
    return suma

if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))