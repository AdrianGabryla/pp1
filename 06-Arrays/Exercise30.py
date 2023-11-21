def bubblesort(tab):
    for i in range(len(tab)-1):
        for j in range(len(tab)-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab
tab = [6,2,8,3,5,7]
print(bubblesort(tab))