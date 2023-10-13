height = float(input("Height in cm: "))
weight = int(input("Weight in kg: "))
bmi = weight/(height/100)**2
bmi_index = True
if bmi >= 18.5 and bmi <= 24.9:
    bmi_index = True
else:
    bmi_index = False
print(f"Your bmi index: {bmi}\nCorrect weight: {bmi_index}")