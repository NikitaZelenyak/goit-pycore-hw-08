from record import Record
def input_error_add_contact(func):
    def wrapper(*args, **kwargs):
        try:
            if len(args[0]) != 2:
                raise ValueError("You must provide both name and phone.")
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
    return wrapper

@input_error_add_contact
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message
