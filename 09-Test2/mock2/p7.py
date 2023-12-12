def f(d,v):
    counter = 0
    for value in d.values():
        if value is not v:
            counter += 1
    return counter

if __name__=="__main__":
    print(f({'a':True,'b':False,'c':True,'d':True,'e':True}, True))
    print(f({'a':True,'b':False,'c':True,'d':True,'e':True}, False))