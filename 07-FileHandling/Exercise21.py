with open("integers.txt", "a") as integers:
    for i in range(1, 51):
        integers.write(str(i)+"\n")