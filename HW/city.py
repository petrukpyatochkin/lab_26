class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

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

    def __repr__(self):
        return (f"City(name='{self.name}', region='{self.region}', country='{self.country}', "
                f"population={self.population}, postal_code='{self.postal_code}', phone_code='{self.phone_code}')")

    def __str__(self):
        return (f"Місто: {self.name}, Регіон: {self.region}, Країна: {self.country}, "
                f"Населення: {self.population}, Поштовий код: {self.postal_code}, Телефонний код: {self.phone_code}")

    def __eq__(self, other):
        return self.name == other.name and self.country == other.country and self.region == other.region

    def __lt__(self, other):
        return self.population < other.population



