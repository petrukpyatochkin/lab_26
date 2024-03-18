import datetime

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print(f"Назва стадіону: {self.name}")
        print(f"Дата відкриття: {self.opening_date.strftime('%d-%m-%Y')}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity} осіб")

    def input_info(self):
        self.name = input("Введіть назву стадіону: ")
        date_input = input("Введіть дату відкриття (дд-мм-рррр): ")
        self.opening_date = datetime.datetime.strptime(date_input, '%d-%m-%Y')
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість: "))

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __eq__(self, other):
        return (self.name == other.name and
                self.country == other.country and
                self.city == other.city)

    def __hash__(self):
        return hash((self.name, self.country, self.city))
