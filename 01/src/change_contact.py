def input_error_change_contact(func):
    def wrapper(*args, **kwargs):
        try:
     
            if len(args) < 2:
                raise ValueError("You must provide name, phone, and new phone.")
            command_args = args[0] 
            if len(command_args) != 3:
                raise ValueError("You must provide name, phone, and new phone.")
            
            name = command_args[0]
            book = args[1]  

            if not book.find(name): 
                raise KeyError(f"Contact '{name}' not found.")

            return func(*args, **kwargs)
        except (KeyError, ValueError) as e:
            return f"Error: {e}"
    return wrapper


@input_error_change_contact
def change_contact(args, book):
    name, phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(phone, new_phone)
        return "Number has been changed."
    return "Contact not found."
