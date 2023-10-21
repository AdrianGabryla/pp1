a=int(input("a="))
b=int(input("b="))
print("*"*b)
for i in range(1,a-1):
    print("*"+" "*(b-2)+"*")
print("*"*b)