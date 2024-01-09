import re
mnumbers = ["A15","-31","7abC","+D1","-gH"]
for i in mnumbers:
        print(re.findall('^[A-Da-d]|"+"|"-"|[1-7].*[A-Da-d]|[1-7]&', i))
