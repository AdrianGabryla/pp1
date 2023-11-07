import range
num = int(input("Enter number: "))
outcome = ""
if range.within_range(num):
    outcome = "yes"
else:
    outcome = "no"
print(f"Number {num} in the range <2,15>: {outcome}")