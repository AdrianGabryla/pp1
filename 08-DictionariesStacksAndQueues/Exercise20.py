import json
f = open("euro.json")
js = json.load(f)
print(f"Date            Buying Rate\n===========================")
for i in js["rates"]:
    print(f"{i['effectiveDate']}      {i['mid']}")
f.close()