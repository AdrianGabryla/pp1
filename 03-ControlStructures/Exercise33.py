dec = int(input("Enter decimal number: "))
bi = ""
while dec > 0:
    if dec%2 == 0:
        bi = "0" + bi
    else:
        bi = "1" + bi
    dec = int(dec/2)
print(bi)