file = open("numbers.txt", "r")
f = file.read()
suma = 0
print("Numbers:", end="")
for line in f.split():
    suma += int(line)
    print(f" {line}", end="")
print()
print(f"Sum: {suma}")
file.close()