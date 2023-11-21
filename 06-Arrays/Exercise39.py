tab = [2,5,7,3,8,43,75,123,81,13]
even = []
odd = []
for i in tab:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even+odd)