num = int(input("Enter the amount in PLN: "))
five = 0
two = 0
one = 0
five = int(num/5)
num = num%5
two = int(num/2)
num = num%2
one = int(num/1)
print(f"5zł - {five}\n2zł - {two}\n1zł - {one}")