file = open("lyrics.txt", "r")
f = file.read()
counter = 0
for line in f.split("\n"):
    counter += 1
print(f"File name: lyrics.txt\nNumber of lines: {counter}")
file.close()