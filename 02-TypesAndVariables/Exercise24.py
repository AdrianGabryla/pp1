registration = input("Enter vehicle registration number: ")
if registration[0]=="K" and registration[1]=="K" or registration[1]=="R":
    print(True)
else:
    print(False)