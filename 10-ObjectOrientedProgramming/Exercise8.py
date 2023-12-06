class Phone():
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = True
        self.used_storage = 0
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def change_storage(self, gb):
        self.used_storage = self.storage - gb

phone = Phone("Apple", "Iphone 13", 128)
phone1 = Phone("Samsung", "a52s", 128)
print(f"My phone is {phone.brand} {phone.model} with {phone.storage}Gb")
phone.on()
phone.change_storage(15)
print(f"Storage availbe: {phone.used_storage}")
print(phone1.brand, phone1.model, phone1.storage)