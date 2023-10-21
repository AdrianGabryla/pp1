quan = 0
suma = 0
mean = 0
i = 1
while i != 0:
    i = int(input("Enter number: "))
    if i == 0:
        break
    quan += 1
    suma = suma + i
    mean = suma/quan
print(f"RESULT: Quantity={quan}, Sum={suma}, Mean={mean}")
