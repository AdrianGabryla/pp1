import re

movie_str = "the evening shows start at 7:00pm and 10:15pm"
txt = []
for i in movie_str.split():
    if i[0] == "e" and i[-1] == "g":
        txt.append(i)
print(txt)