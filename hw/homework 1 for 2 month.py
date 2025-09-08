class Car:
    def __init__(self, model, speed, fuel):
        self.model = model
        self.speed = speed
        self.fuel = fuel

    def driver(self, distance):
        fuel_needed = distance * 0.1
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            return  f"{self.model} проехал {distance} км. Остаток топлива: {self.fuel: .1f} л"
        else:
            return f"{self.model} не может проехать {distance} км. Недостаточно топлива!"

car1 = Car("Tesla Model S", 250, 80)
car2 = Car("Toyota Corolla", 180, 40)

print(car1.driver(100))
print(car2.driver(500)) 