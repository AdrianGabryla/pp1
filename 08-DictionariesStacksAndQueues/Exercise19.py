import json
x = open("students.json")
js = json.load(x)
f = open("limited.json", "w")
mass = []
for student in js:
    mass.append({"name" : student["name"], 'surname' : student["surname"], 'student_id' : student["student_id"]})
json.dump(mass, f, indent=6)
x.close()
f.close()
