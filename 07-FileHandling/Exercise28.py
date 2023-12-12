import re
x = open("lyrics.txt", "r")
f = x.read()
words = re.findall("[a-zA-Z]{6,}", f)
for i in words:
    print(i)