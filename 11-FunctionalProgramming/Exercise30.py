bottles = [508,500,512,499,492,511,503,476,501,509]
def correct(limit):
    return lambda x: abs((x-500))<=500*limit/100
print(f"Bottle capacity:{'':<5}500ml")
print(f"Filling tolerance:{'':<3}2%")
print(f"Filled bottles:{'':<6}{str(bottles)[1:-1]}")
print(f"Incorrectly filled:{'':<2}{(len(bottles)-len(list(filter(correct(2), bottles))))*10}%")

