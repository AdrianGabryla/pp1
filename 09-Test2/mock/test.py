import re
x = open("data.txt", "r", encoding="utf8")
f = x.read()
words = re.findall("^wd$",f)
print(words)