def f(x,y,digit):
    counter = 0
    for i in range(x,y+1):
        if str(digit) in str(i):
            for j in str(i):
                if j == str(digit):
                    counter += 1
    return counter

if __name__=="__main__":
    print(f(10,15,1))
    print(f(28,32,2))
    print(f(100,105,6))
    print(f(100,101,0))

