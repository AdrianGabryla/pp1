price = float(input())
discount = int(input())
print(f"{round(price*(100-discount)/100, 2)}\n{round(price-price*(100-discount)/100, 2)}")