file = open("lyrics.txt", "r")
f = file.read()
copy = open("copy.txt", "a")
for row in f.split("\n"):
    copy.write(row+"\n")
file.close()
copy.close()