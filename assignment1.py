# Smartphone class with encapsulation & inheritance

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


class Smartphone(Device):
    def __init__(self, brand, model, os, price):
        super().__init__(brand, model)   # Inheritance
        self.os = os
        self.__price = price             # 🔒 Encapsulated (private attribute)

    def call(self, contact):
        print(f"📞 Calling {contact} from {self.device_info()}...")

    def get_price(self):  # controlled access
        return self.__price

    def set_price(self, new_price):  # setter with control
        if new_price > 0:
            self.__price = new_price
        else:
            print("❌ Price must be positive")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", "Android", 1000)
phone1.call("Alice")
print("Price:", phone1.get_price())
phone1.set_price(1200)
print("Updated Price:", phone1.get_price())
