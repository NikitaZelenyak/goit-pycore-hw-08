
def input_error_show_phone(func):
    def wrapper(*args, **kwargs):
        name = args[0] 
        try:
            if(len(name) == 0):
                raise ValueError("You must provide name.")
             
            book = args[1]  
            if not book.find(name):
                raise KeyError(f"Contact '{name}' not found.")
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: {e}"
    return wrapper
@input_error_show_phone
def show_phone(name, book):
    return book.find(name)