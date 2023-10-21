num = int(input("Number of products purchased: "))
price = int(input("Product price: "))
discount = 0
if num>2:
    discount = (num-2)*price*0.25
print(f"Amount to pay: {num*price-discount}")
