x = int(input("x = "))
y = int(input("y = "))
quadrant = 0
if x >= 0 and y >= 0:
    quadrant = 1
elif x < 0 and y >= 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
else:
    quadrant = 4
print(f"Number of quadrant in the coordinate system is {quadrant}")

