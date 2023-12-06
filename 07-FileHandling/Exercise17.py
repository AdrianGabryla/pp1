file = open("lyrics.txt", "r")
f = file.read()
f = f.split("\n")
enter = True
counter = 0
while enter:
    key = input("Press enter to continue: ")
    if key !=  "":
        enter = False
    else:
        for row in range(counter, counter+5):
            print(f[counter])
            counter += 1
            
file.close()