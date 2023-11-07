def f(dice):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for i in dice:
        if i == "1":
            one =+ 1
        if i == "2":
            two =+ 1
        if i == "3":
            three =+ 1
        if i == "4":
            four =+ 1
        if i == "5":
            five =+ 1
        if i == "6":
            six =+ 1
    tab = [one, two ,three, four, five, six]
    tab.sort()
    if tab[-1] == one:
        return 1
    if tab[-1] == two:
        return 2
    if tab[-1] == three:
        return 3
    if tab[-1] == four:
        return 4
    if tab[-1] == five:
        return 5
    if tab[-1] == six:
        return 6
    
print(f("5233165554211"))
    
        