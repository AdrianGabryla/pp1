first_name = input("Enter first person name: ")
first_age = int(input("Enter first person age: "))
second_name = input("Enter second person name: ")
second_age = int(input("Enter second person age: "))
if first_age >= 18 and second_age >= 18:
    print(f"Both {first_name} and {second_name} are adults")
else:
    print(f"Either {first_name} or {second_name} is not adult")