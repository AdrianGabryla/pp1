import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
cir = a+b+c
p = cir/2
area = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Triangle area: {area}\nTriangle circumference: {cir}")