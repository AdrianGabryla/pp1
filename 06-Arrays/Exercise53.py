def identity_matrix(n):
    tab = []
    for row in range(n):
        tab.append([])
        for col in range(n):
            tab[row].append(0)
    for i in range(len(tab)):
        tab[i][i] = 1
    return tab
def matrix(tab):
    tab1 = ""
    for row in range(len(tab)):
        for col in range(len(tab)):
            tab1 = tab1 + str(tab[row][col])
print(matrix(identity_matrix(5)))