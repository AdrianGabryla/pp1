tab = [48,47,54,50,42,68,39,46]
speed = list(filter(lambda x: x>50, tab))
print(tab)
print(f"Speed too high: {speed}")