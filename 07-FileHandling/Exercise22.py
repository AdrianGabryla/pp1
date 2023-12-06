import random
with open("randomint.txt", "a") as r:
    for i in range(50):
        r.write(str(random.randint(100,999))+"\n")