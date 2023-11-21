def create_2d_arr(x, y):
    tab = []
    for i in range(x):
        tab.append([])
        for j in range(y): 
            tab[i].append(0)
    return tab
print(create_2d_arr(3,5))