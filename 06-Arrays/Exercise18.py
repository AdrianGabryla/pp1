tab = [[True,False],[True,True],[False,False]]
for row in tab:
    for element in row:
        if element:
            element = False
        else:
            element = True
print(tab)