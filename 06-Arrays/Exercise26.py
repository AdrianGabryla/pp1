tab = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest = 0
name = ""
for i in range(len(tab)):
    if len(tab[i]) > longest:
        longest = len(tab[i])
        name = tab[i]
print(name)