tab = [[2,5,4],[9,0,3]]
print(tab)
row = len(tab)
columns = len(tab[0])
print(f"Rows: {row}\nColumns: {columns}")
print(tab[0][1])
print(tab[1][2])
for i in tab[1]:
    print(i, " ", end="")