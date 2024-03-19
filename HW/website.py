class Website:
    def __init__(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description

    def display_info(self):
        print(f"Назва вебсайту: {self.name}")
        print(f"Адреса: {self.url}")
        print(f"Опис: {self.description}")

    def __str__(self):
        return f"Вебсайт '{self.name}': {self.url} - {self.description}"

    def __eq__(self, other):
        return self.url == other.url

    def __hash__(self):
        return hash(self.url)
