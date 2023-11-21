def compare(tab1, tab2):
    if len(tab1) == len(tab2):
        for i in range(len(tab1)):
            if tab1[i] != tab2[i]:
                return False
        return True
    return False

tab1 = ["water","book","sky"]
tab2 = ["water","book","sky"]
print(compare(tab1, tab2))
tab3 = [True,False]
tab4 = [True,False,True]
print(compare(tab3, tab4))
tab5 = [5,3,1]
tab6 = [5,3,1]
print(compare(tab5, tab6))
tab7 = [3,2,1]
tab8 = [3,2]
print(compare(tab7, tab8))