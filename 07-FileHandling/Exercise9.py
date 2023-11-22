file = open("countries.txt", "r")
f = file.read()
x = 0
for i in f.split():
    x += 1
    print(f"{x}. {i}")
file.close()
