tab = [1,23,5,382,1,17,4,906]
print("-----------------------------------------")
print(f"|", end="")
for i in tab:
    if len(str(i)) == 3:
        print(f" {i}|", end="")
    elif len(str(i)) == 2:
        print(f"  {i}|", end="")
    else:
        print(f"   {i}|", end="")
print()
print("-----------------------------------------")