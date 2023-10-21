i = 1
while i<=3:
    num = input("Enter number: ")
    if num != "0805":
        print("Incorrect...")
        i += 1
    else:
        print("Correct!!!")
        i=5
if i==4:
    print("Sorry, your payment card has been blocked.")