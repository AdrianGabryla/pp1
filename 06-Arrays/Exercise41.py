tab = [1,23,5,382,1,17,4,906]
tab1 = [1,382, 69]
def f(tab, tab1):
    for i in tab1:
        if i not in tab:
            return False
    return True
print(f(tab, tab1))