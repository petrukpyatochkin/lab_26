from datetime import datetime

from stadium import Stadium

import datetime


def __eq__(self, other):
    return self.name == other.name and self.country == other.country and self.city == other.city


def get_date(prompt):
    while True:
        try:
            date_input = input(prompt)
            return datetime.datetime.strptime(date_input, '%d-%m-%Y')
        except ValueError:
            print("Неправильний формат дати. Використовуйте дд-мм-рррр.")


def main():
    stadiums = []

    while True:
        print("\nМеню:")
        print("1. Додати стадіон")
        print("2. Порівняти стадіони")
        print("3. Показати інформацію про всі стадіони")
        print("4. Вийти з програми")
        choice = input("Введіть номер опції: ")

        if choice == '1':
            name = input("Введіть назву стадіону: ") or 'Стадіон 1'
            country = input("Введіть країну: ") or 'Країна 1'
            city = input("Введіть місто: ") or 'Місто 1'

            temp_stadium = Stadium(name, None, country, city, 0)

            if temp_stadium in stadiums:
                print("Стадіон з такою назвою вже існує.")
            else:
                opening_date = get_date("Введіть дату відкриття (дд-мм-рррр): ")
                capacity = int(input("Введіть місткість: "))
                stadium = Stadium(name, opening_date, country, city, capacity)
                stadiums.append(stadium)
                print(f"Стадіон '{name}' було успішно додано.")

        elif choice == '2':
            if len(stadiums) < 2:
                print("Необхідно мінімум два стадіони для порівняння.")
            else:
                stadium_names = [s.name for s in stadiums]
                print("Доступні стадіони для порівняння: ", ", ".join(stadium_names))
                name1 = input("Введіть назву першого стадіону для порівняння: ")
                name2 = input("Введіть назву другого стадіону для порівняння: ")
                stadium1 = next((s for s in stadiums if s.name == name1), None)
                stadium2 = next((s for s in stadiums if s.name == name2), None)
                if not stadium1 or not stadium2:
                    print("Один або обидва стадіони не знайдені.")
                else:
                    if stadium1 < stadium2:
                        print(f"{stadium1.name} менший за {stadium2.name} за місткістю.")
                    elif stadium1 == stadium2:
                        print(f"{stadium1.name} та {stadium2.name} мають однакову місткість.")
                    else:
                        print(f"{stadium1.name} більший за {stadium2.name} за місткістю.")

        elif choice == '3':
            if not stadiums:
                print("Ще не додано жодного стадіону.")
            else:
                for s in stadiums:
                    s.display_info()

        elif choice == '4':
            break

        else:
            print("Введено некоректну опцію, спробуйте знову.")

        user_choice = input(
            "\nНатисніть Enter, щоб повернутися до головного меню, або будь-яку іншу клавішу, щоб вийти: ")
        if user_choice:
            break


if __name__ == "__main__":
    main()
