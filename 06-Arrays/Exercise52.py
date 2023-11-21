tab = [
    [-38,19,3,4,2], 
    [5,40,7,5,56],
    [-7,11,23,78,1]
]
print(tab)
for i in range(len(tab)):
    tab[i][0], tab[i][-1] = tab[i][-1], tab[i][0]
print(tab)