cur_price = int(input("Current price: "))
pre_price = int(input("Previous price: "))
red = 100-(cur_price/pre_price*100)
if red >= 10:
    print(f"Buy the product!!\nProduct price reduced by {int(red)}%")
else:
    print("Dont't buy")