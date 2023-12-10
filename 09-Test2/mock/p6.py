import json
def f(years, course):
    f = open("data.json")
    js = json.load(f)
    counter = 0
    for i in js:
        avg = 0
        if i["age"] >= years:
            for j in i["studies"]["courses"]:
                if j["name"] == course:
                    for x in j["grades"]:
                        avg += x
                    if avg >= 4:
                        counter += 1
    f.close()
    return counter

if __name__=="__main__":
    print(f(21, "statistics"))