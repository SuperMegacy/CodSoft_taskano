class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr_(self):
        return f"Contact(Name: {self.name}, Phone: {self.phone}"
