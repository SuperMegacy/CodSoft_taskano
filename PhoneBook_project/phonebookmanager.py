from phonebook import PhoneBook

class PhoneBookManager:
    def __init__(self):
        self.phone_book = PhoneBook()


    def menu(self):
        print("\n\tWelcome to PhoneBook")
        print("\n=== Phone Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")


    def run(self):
        while True:
            self.menu()

            user_choice = input('Enter your choice: ').strip()

            if user_choice == '1':
                name = input("Enter contact name: ").strip()
                phone_number = input("Enter phone number: ").strip()
                self.phone_book.add_contact(name, phone_number)

            elif user_choice == '2':
                self.phone_book.display_contacts()

            elif user_choice == '3':
                name = input("Enter contact name to search: ").strip()
                self.phone_book.find_contact(name)

            elif user_choice == '4':
                name = input("Enter contact name to delete: ").strip()
                self.phone_book.remove_contact(name)

            elif user_choice == '5':
                print("Exiting phone book. Goodbye!")
                break

            else:
                 print("Invalid option, please try again.")
