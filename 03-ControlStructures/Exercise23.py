dogs_age = int(input("Enter the dog's age in human years: "))
if dogs_age == 1:
    print("Dog's age: 10.5")
elif dogs_age == 2:
    print("Dog's age: 21")
elif dogs_age > 2:
    dogs_age -= 2
    print(f"Dog's age: {dogs_age*4+21}")