class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Двигун {self.brand} {self.model} {self.year} року запущено.")

    def __repr__(self):
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year})"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __add__(self, other):
        if self.brand == other.brand:
            new_model = f"{self.model} & {other.model}"
            new_year = max(self.year, other.year)
            return Car(self.brand, new_model, new_year)
        else:
            print("Cannot combine cars of different brands.")
            return None

car1 = Car("Toyota", "Camry", 2018)
car2 = Car("Toyota", "Corolla", 2020)
car3 = Car("Ford", "Mustang", 2020)

car1.start_engine()
print(car1)

print(car1 == car2)
print(car1 < car2)

new_car = car1 + car2
if new_car is not None:
    print(new_car)

car1 + car3
