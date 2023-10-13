password = input("Enter password: ")
count = len(password)
valid = True
if count == 8:
    valid = True
else: 
    valid = False
print("Password is valid: ", valid)