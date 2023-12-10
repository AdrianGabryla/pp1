import json
f = open("data.json")
js = json.load(f)
for i in js:
    if i["age"] >= 21:
        for j in i["studies"]["courses"]:
            if j["name"] == "statistics":
                print(j["grades"])
