class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def display_info(self):
        print("\n")
        for key, value in self.__dict__.items():
            if value is not None:
                print(f"{key.replace('_', ' ').capitalize()}: {value}")

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Поле '{key}' не існує в класі City.")

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
        else:
            print(f"Місто {city} вже є у списку.")

    def remove_city(self, city):
        try:
            self.cities.remove(city)
        except ValueError:
            print(f"Місто {city} не знайдено у списку.")

    def __repr__(self):
        return (f"Country(name='{self.name}', continent='{self.continent}', population={self.population}, "
                f"phone_code='{self.phone_code}', capital='{self.capital}', cities={self.cities})")

    def __str__(self):
        cities_str = ", ".join(self.cities)
        return (f"Країна: {self.name}\nКонтинент: {self.continent}\nНаселення: {self.population}\n"
                f"Телефонний код: {self.phone_code}\nСтолиця: {self.capital}\nМіста: {cities_str}")

    def __eq__(self, other):
        return self.name == other.name and self.continent == other.continent

