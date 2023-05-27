class Car:
    def __init__(self, company="Toyota", color="Green"):
        self.company = company
        self.color = color


car1 = Car()
car2 = Car(color="Blue")
print(car1.color, car1.company)
print(car2.color, car2.company)