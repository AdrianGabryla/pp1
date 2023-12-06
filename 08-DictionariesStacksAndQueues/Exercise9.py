countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":83000000},
    {"name":"France", "population":64000000},
    {"name":"UK", "population":67000000},
    {"name":"Italy", "population":59000000}
]
i = 0
while i < len(countries):
    print(countries[i]["name"], countries[i]["population"])
    i += 1