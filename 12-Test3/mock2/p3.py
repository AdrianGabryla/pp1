def f(d):
    suma = 0
    for key in d.values():
        suma += key
    avg = suma/len(d)
    counter = 0
    for key in d.values():
        if key > avg:
            counter += 1
    return counter

if __name__=="__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30}))