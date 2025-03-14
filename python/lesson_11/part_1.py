class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self):
        return super().seating_capacity(50)

bus = Autobus("Renaul Logan", 180, 12)

print(bus.seating_capacity())