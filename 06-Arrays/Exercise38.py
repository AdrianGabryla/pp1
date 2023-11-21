tab = [2,5,7,3,8,43,75,123,81,13]
num = int(input("Podaj numer: "))
out = 0
for i in tab:
    if i > num:
        out += 1
print(out)