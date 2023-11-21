def f(number, tab):
    if number in tab:
        return True
    return False
tab = [15, 38, 7, 23, 14]
num = int(input("Number: "))
print(f"Array: {tab}")
if f(num,tab):
    print(f"Result: number {num} appears in the array")
else:
    print(f"Result: number {num} doesn't appear in the array")