file = open("lyrics.txt", "r")
f = file.read()
f = f.split("\n")
print(f[2])