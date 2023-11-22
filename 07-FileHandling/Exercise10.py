file = open("lyrics.txt", "r")
f = file.read()
for line in f.split("\n"):
    print(line)
file.close()