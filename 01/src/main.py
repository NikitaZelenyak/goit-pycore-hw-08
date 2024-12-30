
from add_contact import add_contact
from change_contact import change_contact
from parse_input import parse_input
from show_phone import show_phone
from show_all import show_all
from add_birthday import add_birthday
from get_upcoming_birthdays import get_upcoming_birthdays
from show_birthday import show_birthday

from save_data import save_data
from load_data import load_data
def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args[0], book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
           print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
          print(get_upcoming_birthdays(book))

        else:
            print("Invalid command.")
        
        save_data(book)

if __name__ == "__main__":
    main()
