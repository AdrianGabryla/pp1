def transpose_matrix(m):
    for row in range(len(m)):
        for col in range(row, len(m[row])):
            m[row][col], m[col][row] = m[col][row], m[row][col]
    return m
tab = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
tab1 = [
    [1,2,3,4,5],
    [6,7,8,9,0]
]
tab2 = [
    [5,6,7,8]
]
print(transpose_matrix(tab))