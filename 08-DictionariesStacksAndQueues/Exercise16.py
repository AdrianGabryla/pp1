Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]
krk = ""
avgk = 0
spt = ""
avgs = 0
for i in range(len(hotels_in_Sopot)):
    krk = krk + Hotels_in_Krakow[i]["name"] + ", "
    spt = spt + hotels_in_Sopot[i]["name"] + ", "
    avgk += Hotels_in_Krakow[i]["price"]
    avgs += hotels_in_Sopot[i]["price"]
cheaper = ""
if avgs < avgk:
    cheaper = "Sopot"
else:
    cheaper = "Kraków"
print(f"Hotels in Krakow: {krk}\nAverage hotel price in Krakow: {avgk/len(Hotels_in_Krakow)}\nHotels in Sopot: {spt}\nAverage hotel price in Sopot: {avgs/len(hotels_in_Sopot)}\nCheaper hotels in: {cheaper}")