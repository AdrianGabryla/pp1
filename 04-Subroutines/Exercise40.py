def f(n):
    suma = 0
    tab = []
    for letter in str(n):
        tab.append(int(letter))
    lenght = len(tab)
    for i in range(len(tab)):
        for j in range(i+1, lenght):
            if tab[i] == tab[j]:
                suma += tab[j]
                tab.pop(tab[j])
                lenght -= 1
    return suma

print(f(230335))
print(f(513553007))