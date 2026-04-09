
from collections import UserDict
from colorama import Fore, Style, init
init(autoreset=True)

# OOP AddressBook inherits from UserDict to manage records like a dictionary
class AddressBook(UserDict):
    # functions to add, find, delete, edit records within the book
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)
# funtion to display result user-friendly
    def __str__(self):
        if not self.data:
            return "Address book is empty."
        return '\n'.join(str(record) for record in self.data.values())

# classes to build AddressBook with
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    # Phone validation is done in constructor to ensure data integrity
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)
# class Record is used to manage single record of name and phone
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_number = Phone(phone)
        self.phones.append(phone_number)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        phone_remove = self.find_phone(phone)
        if phone_remove:
            self.phones.remove(phone_remove)

    def edit_phone(self, old_phone, new_phone):
        phone_number = self.find_phone(old_phone)
        if not phone_number:
            raise ValueError("Phone number not found")
        new_phone_number = Phone(new_phone)
        phone_number.value = new_phone_number.value

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

# function to read user requests
def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:]
    return command, args

# function to add contacts taking input from user
def add_contact(args, contacts):
    if len(args) < 2:
        return "Please enter name and phone number."

    name, phone = args[0], args[1]

    try:
        record = contacts.find(name)

        if record is None:
            record = Record(name)
            record.add_phone(phone)
            contacts.add_record(record)
            return "Contact added."
        else:
            record.add_phone(phone)
            return "Phone added to existing contact."

    except ValueError as e:
        return str(e)
    
# function to change contacts
def change_contact(args, contacts):
    if len(args) < 3:
        return "Please enter name, old phone, and new phone."

    name, old_phone, new_phone = args[0], args[1], args[2]

    record = contacts.find(name)
    if record is None:
        return "Contact not found."

    try:
        record.edit_phone(old_phone, new_phone)
        return "Phone changed successfully."
    except ValueError as e:
        return str(e)


def show_phone(args, contacts):
    if len(args) < 1:
        return "Please enter a contact name."

    name = args[0]
    record = contacts.find(name)

    if record is None:
        return "Contact not found."

    if not record.phones:
        return "No phones found for this contact."

    return '; '.join(phone.value for phone in record.phones)


def show_all(contacts):
    return str(contacts)

def delete_contact(args, contacts):
    if len(args) < 1:
        return "Please enter a contact name."

    name = args[0]

    if contacts.find(name) is None:
        return "Contact not found."

    contacts.delete(name)
    return "Contact deleted."

# function to store contacts in the file
def save_data(book, filename="contact_list.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for name, record in book.data.items():
            phones = ",".join(phone.value for phone in record.phones)
            file.write(f"{name}:{phones}\n")

# function to load data from the file, read contacts
def load_data(filename="contact_list.txt"):
    book = AddressBook()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(":")
                if len(parts) != 2:
                    continue

                name, phones_str = parts
                record = Record(name)

                if phones_str:
                    phones = phones_str.split(",")
                    for phone in phones:
                        if phone:
                            record.add_phone(phone)

                book.add_record(record)

    except FileNotFoundError:
        pass

    return book

# main function which operates with classes, methods and functions to communicate with user, process user input and manage contacts in the contact book
def main():
    contacts = load_data()
    print("🤖 Welcome to the assistant bot!")

    while True:
        user_input = input(
            "Enter a command "
            + Fore.CYAN + Style.BRIGHT
            + "add, change, phone, all, delete, exit: "
            + Style.RESET_ALL
        ).strip()

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(contacts)
            print("🤖 Good bye!")
            break
        elif command == "hello":
            print("🤖 How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            save_data(contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            save_data(contacts)
            print(result)
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "delete":
            result = delete_contact(args, contacts)
            save_data(contacts)
            print(result)
        else:
            print("🤨 Invalid command.")
if __name__ == "__main__":
    main()

