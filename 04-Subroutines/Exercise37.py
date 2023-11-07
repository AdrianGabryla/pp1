def f(n):
    n1=0
    n2=1
    suma = 0
    if n == 2:
        suma = 1
        return suma
    for i in range(n-2):
        suma = n1 + n2
        n1 = n2
        n2 = suma
    return suma
print(f(9))