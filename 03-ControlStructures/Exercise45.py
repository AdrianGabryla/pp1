num = int(input("Podaj zakres: "))
prime = ""
for i in range(2, num+1):
    for j in range(2, i):
        if i%j==0:
            break
    else:
        prime = prime+ " " + str(i)
print(prime)