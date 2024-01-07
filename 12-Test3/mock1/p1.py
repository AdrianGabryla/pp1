word = "book"
out = ""
for i in range(len(word)):
    if i == 0:
        out = word.capitalize() + "-"
    elif i == len(word)-1:
        out = out + word[:-1] + word[-1].upper()
    else:
        out = out + word[:i] + word[i].upper() + word[i+1:] + "-"
print(out)
