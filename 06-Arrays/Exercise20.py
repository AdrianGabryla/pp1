tab = [34,7,19,4,21,8]
i = 0
even = 0
while i < len(tab):
    if tab[i]%2==0:
        even += 1
    i += 1
print(even)