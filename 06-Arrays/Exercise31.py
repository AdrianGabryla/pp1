tab = [2, 3, 2, 5, 8, 1, 9, 8]
tab1= []
for i in range(len(tab)):
    if tab[i] not in tab[i+1:] and tab[i] not in tab[:i-1]:
        tab1.append(tab[i])
print(tab1)