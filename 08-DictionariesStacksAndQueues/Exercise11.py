import json
movie = {
    "title":"Example",
    "year": 2000,
    "actor":{"leading":"Leonardo","supporting":"Brad"},
    "oscar":False,
    "director":"Quentin"
}
f = open("favourite.json", "w")
json.dump(movie, f, indent=6)
f.close()
