meat_and_fish = open("MeatAndFish.txt", "r")
m = meat_and_fish.read()
grains_and_bread = open("GrainsAndBread.txt", "r")
g = grains_and_bread.read()
ap = open("allproducts.txt", "a")
for row in m.split("\n"):
    ap.write(row+"\n")
for row in g.split("\n"):
    ap.write(row+"\n")
meat_and_fish.close()
grains_and_bread.close()
ap.close()