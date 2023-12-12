import re
x = open("grades.txt", "r")
f = x.read()
grades = re.findall("\d.\d", f)
avg = 0
for i in grades:
    avg += float(i)
print(avg/len(grades))