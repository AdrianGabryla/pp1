winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}
out = 0
for value in winter_semester.values():
    out += value
print(f"The total number of hours in the winter semester is {out}.")