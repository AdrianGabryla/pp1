tab = [12,6,4,9,10]
def star(n):
    return "*"*n
for i in tab:
    if i<10:
        print(f" {i}: {star(i)}")
    else:
        print(f"{i}: {star(i)}")