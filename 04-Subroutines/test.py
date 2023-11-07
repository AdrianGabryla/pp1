def f(n):
    suma = 0
    n = str(n)
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] == n[j]:
                suma += int(n[j])
        n = n.replace(n[i], "")
    return suma

print(f(230335))
print(f(513553007))