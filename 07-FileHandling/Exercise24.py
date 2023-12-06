import csv
with open("studentlist.csv", "r") as x:
    f = csv.DictReader(x)
    for row in f:
        if int(row["age"]) < 30:
            print(f"{row['first_name']} {row['last_name']}  {row['email']}")