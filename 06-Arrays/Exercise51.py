tab = [
    [-38,19,3,4,2], 
    [5,40,7,5,56],
    [-7,11,23,78,1]
]
print(tab)
tab1 = tab[0]
tab[0]=(tab[-1])
tab[-1]=(tab1)
print(tab)