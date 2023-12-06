import json
f = open("products.csv", "r")
csv = f.read()
js = open("products.json", "w")
mass = []
for i in csv.split():
    print(i)
f.close()
js.close()