def numbers(n):
    x = ""
    for i in range(1, int(n)+1):
        x = x + str(i) + " "
    return x
print(f"Numbers <1,15>: {numbers(15)}\nNumbers <1,7>: {numbers(7)}")

