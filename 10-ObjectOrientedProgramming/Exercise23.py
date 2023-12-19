class C():
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
    def data(self):
        if self.age >= 18:
            return f"{self.surname.upper()}{self.name.upper()[0]}{self.seniority}"
        elif self.age < 18:
            return f"{self.surname.lower()}{self.name.lower()[0]}{self.seniority}"
        
x = C("Anna","May",17,7)
y = C("George","Brown",21,4)
print(x.data())
print(y.data())