class Watch:
    def __init__(self, model, manufacturer, year, price, watch_type):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def display_info(self):
        print(f"Модель: {self.model}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Рік випуску: {self.year}")
        print(f"Ціна: {self.price} грн")
        print(f"Тип: {self.watch_type}")

    def __str__(self):
        return (f"Модель: {self.model}, Виробник: {self.manufacturer}, "
                f"Рік випуску: {self.year}, Ціна: {self.price} грн, Тип: {self.watch_type}")

    def __eq__(self, other):
        return (self.model == other.model and self.manufacturer == other.manufacturer and
                self.year == other.year and self.price == other.price and self.watch_type == other.watch_type)

    def __lt__(self, other):
        return self.price < other.price

    def __hash__(self):
        return hash((self.model, self.manufacturer, self.year, self.price, self.watch_type))
