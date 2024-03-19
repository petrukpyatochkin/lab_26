class Human:
    def __init__(self, full_name, birth_date, phone_numbers, address):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone_numbers = phone_numbers
        self.address = address

    def update_human(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Поле '{key}' не існує в класі Human.")

    def add_phone_number(self, phone_number):
        self.phone_numbers.append(phone_number)

    def remove_phone_number(self, phone_number):
        if phone_number in self.phone_numbers:
            self.phone_numbers.remove(phone_number)
        else:
            print("Номер не знайдено.")

    def update_address_info(self, **kwargs):
        self.address.update_address(**kwargs)

    def display_info(self):
        print("\n")
        for key, value in self.__dict__.items():
            if value is not None:
                if key == 'address':
                    value.display_address()
                elif key == 'phone_numbers':
                    print(f"{key.replace('_', ' ').capitalize()}: {', '.join(value)}")
                else:
                    print(f"{key.replace('_', ' ').capitalize()}: {value}")

    def __repr__(self):
        return (f"Human(full_name='{self.full_name}', "
                f"birth_date='{self.birth_date.strftime('%d-%m-%Y')}', "
                f"phone_numbers={self.phone_numbers}, "
                f"address='{self.address}')")

    def __str__(self):
        return (f"Людина: {self.full_name}\n"
                f"Дата народження: {self.birth_date.strftime('%d-%m-%Y')}\n"
                f"Телефонні номери: {', '.join(self.phone_numbers)}\n"
                f"Адреса: {self.address}\n")

    def __eq__(self, other):
        return self.full_name == other.full_name and self.birth_date == other.birth_date

    def __lt__(self, other):
        return self.birth_date < other.birth_date
