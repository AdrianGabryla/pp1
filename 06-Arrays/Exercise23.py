tab = [-15, 8, -31, 47, -2, 19]
maks = tab[0]
mini = tab[0]
for i in tab:
    if maks < i:
        maks = i
    if mini > i:
        mini = i
print(f"Max: {maks}\nMin: {mini}")