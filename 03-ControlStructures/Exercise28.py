num = input("Enter EAN-13 articel number: ")
lenght = len(num)
if lenght == 13:
    print("Article number is correct")
    if num[:3] == "590":
        print("Article manufactured in Poland")
    else:
        print("Not polish")
else:
    print("Incorrect number")