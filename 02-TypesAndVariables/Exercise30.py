import random
x = random.randint(1,6)
special_number = True
if x == 6:
    special_number = True
else:
    special_number = False
print(f"Dice rolled: {x}\nSpecial number: {special_number}")