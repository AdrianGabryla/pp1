num = input()
dec = 0
for i in range(1,5):
    if (num[-i])=="0":
        continue
    else:
        x=2**(i-1)
        dec = dec + x
print(dec)

