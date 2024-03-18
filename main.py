from fraction import Fraction


def get_fraction(prompt):
    while True:
        try:
            numerator, denominator = map(int, input(prompt).split())
            return Fraction(numerator, denominator)
        except Exception as e:
            print(f"Помилка вводу: {e}. Спробуйте ще раз.")


while True:
    try:
        fraction1 = get_fraction("Введіть чисельник та знаменник першого дробу через пробіл: ")
        fraction2 = get_fraction("Введіть чисельник та знаменник другого дробу через пробіл: ")

        print("Оберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        operation = input("Введіть номер операції: ")

        if operation == '1':
            result = fraction1 + fraction2
        elif operation == '2':
            result = fraction1 - fraction2
        elif operation == '3':
            result = fraction1 * fraction2
        elif operation == '4':
            result = fraction1 / fraction2
        else:
            print("Невідома операція.")
            continue

        print("Результат: ", result)

    except Exception as e:
        print(f"Сталася помилка: {e}")
        continue

    user_choice = input("\nНатисніть Enter, щоб продовжити, або будь-яку іншу клавішу, щоб вийти: ")
    if user_choice:
        break
