dic = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
cities = list(filter(lambda x: x[1]>0, dic.items()))
print(f"Cities with positive temperatures: {[x[0] for x in cities]}")
