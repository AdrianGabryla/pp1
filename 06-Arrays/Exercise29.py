tab = []
tab1 = [4,36,12,28,9,44,5]
tab2 = [5,1,36]
for i in range(len(tab1)):
    if tab1[i] not in tab2:
        tab.append(tab1[i])
print(tab)