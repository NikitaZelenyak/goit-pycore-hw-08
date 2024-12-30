def show_birthday(args,book):
    name, *_  = args
    record = book.find(name)
    if not record:
        return f"No contact found with the name '{name}'."
    if record.birthday:
        return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}."
    else:
        return f"{name} does not have a birthday recorded."