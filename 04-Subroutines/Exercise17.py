def different(n1,n2,n3):
    if n1!=n2 and n1!=n3 and n2!=n3:
        return True
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")
if different(a,b,c):
    print(f"Numbers {a}, {b} and {c} are different ")
else:
    print(f"Numbers {a}, {b} and {c} aren't different")