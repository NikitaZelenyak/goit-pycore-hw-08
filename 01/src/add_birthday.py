from birthday import Birthday
def input_error_add_birthday(func):
    def wrapper(*args, **kwargs):
        try:
           
            name, date = args[0]
        except ValueError:
            return "Error: Please provide both a name and a birthday date in the format 'dd.mm.yyyy'."
        
        try:
            Birthday(date) 
        except ValueError:
            return "Error: Invalid date format. Please use 'dd.mm.yyyy'."
        
        return func(*args, **kwargs)
    return wrapper

@input_error_add_birthday
def add_birthday(args, book):
    name , date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return f"Birthday added for {name}."
    else:
        return f"Error: Contact '{name}' not found in the address book."
