import random
class thermometer():
    def __init__(self):
        self.temp = round(random.uniform(34,43), 1)
        self.power = False
    def temp_on(self):
        self.power = True
    def temp_off(self):
        self.power = False
    def give(self):
        if self.power:    
            if self.temp >= 41:
                return f"Temp-{self.temp}C: Fever CRITICAL TEMPERATURE"
            elif self.temp >= 37:
                return f"Temp-{self.temp}C: Fever"
            else:
                return f"Temp-{self.temp}C"