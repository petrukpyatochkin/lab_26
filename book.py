class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}\n")


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

    def __repr__(self):
        return f"Книга(Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre})"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.genre == other.genre

    def __lt__(self, other):
        return self.title < other.title

    def __add__(self, other):
        if self.genre == other.genre:
            new_title = f"{self.title} & {other.title}"
            new_author = f"{self.author} & {other.author}"
            return Book(new_title, new_author, self.genre)
        else:
            print("Не можна додавати книги різних жанрів.")
            return None


book1 = Book("Книга 1", "Автор 1", "Жанр 1")
book2 = Book("Книга 2", "Автор 2", "Жанр 2")
book3 = Book("Книга 3", "Автор 3", "Жанр 3")

book1.display_info()
print(book1)

print(book1 == book2)
print(book1 < book2)

new_book = book1 + book2
if new_book is not None:
    new_book.display_info()

book1 + book3
