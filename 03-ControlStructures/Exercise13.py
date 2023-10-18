num_one = int(input("Enter number: "))
num_two = int(input("Enter number: "))
if num_one >= 0 or num_two >= 0:
    print(f"At least one of entered numbers {num_one} or {num_two} is not negative")
else:
    print("Both negative")
