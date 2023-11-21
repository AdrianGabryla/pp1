tab = [
    [-38, 19], 
    [5,40],
    [-7,11],
    [29,16]
]
xs = 0
ys = 0
xl = 0
yl = 0
s = 0
l = 0
for row in range(len(tab)):
    for col in range(len(tab[row])):
        if l < tab[row][col]:
            xl = row
            yl = col
            l = tab[row][col]
        if s > tab[row][col]:
            xs = row
            ys = col
            s = tab[row][col]
print(f"Smallest location: [{xs+1}][{ys+1}]\nLargest location: [{xl+1}][{yl+1}]")