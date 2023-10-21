washing_product = input("Product type: ")
rinse = input("rinse = ")
spin = input("spin = ")
print(rinse)
print(spin)
time = 0
if washing_product == "jacket":
    time = 40
elif washing_product == "underwear":
    time = 70
elif washing_product == "shoes":
    time = 20
if rinse == "True":
    time = time + 15
if spin == "True":
    time = time + 9
print(time)