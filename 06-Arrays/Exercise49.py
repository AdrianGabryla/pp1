tab = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
for row in range(1, len(tab)+1):
    for column in range(1, len(tab)+1):
        tab[row-1][column-1] = (column*row)
print(tab)