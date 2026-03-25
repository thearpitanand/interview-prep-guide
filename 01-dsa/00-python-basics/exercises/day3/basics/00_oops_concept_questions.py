class Car:

    def __init__(self, brand, model, **kwargs):
        super().__init__(**kwargs)
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    @staticmethod
    def general_description():
        return f"A car is a vehicle that is used to transport people and goods. "

    @property
    def brand(self):
        return self.__brand

    def set_brand(self, brand):
        if brand and self.__brand is not None:
            self.__brand = brand
        else:
            raise ValueError("Brand cannot be None or already set")


class Battery:

    def __init__(self, battery_capacity, **kwargs):
        super().__init__(**kwargs)
        self.battery_capacity = battery_capacity

    def get_battery_capacity(self):
        return self.battery_capacity + " kWh"


class Engine:

    def __init__(self, engine_type, **kwargs):
        super().__init__(**kwargs)
        self.engine_type = engine_type


class ElectricCar(Car, Battery, Engine):

    def __init__(self, brand, model, battery_capacity, engine_type):
        super().__init__(
            brand=brand,
            model=model,
            battery_capacity=battery_capacity,
            engine_type=engine_type,
        )

    def full_name(self):
        return f"{super().full_name()} with {super().get_battery_capacity()} battery"


tata_nexon_ev = ElectricCar("Tata", "Nexon", "85", "Electric")

print(tata_nexon_ev.full_name())
print(tata_nexon_ev.brand)
print(tata_nexon_ev.set_brand("Tata 2"))
print(tata_nexon_ev.full_name())
print(isinstance(tata_nexon_ev, Car))
print(tata_nexon_ev.get_battery_capacity())
print(tata_nexon_ev.engine_type)

print(type(tata_nexon_ev).__name__ is ElectricCar.__name__)
