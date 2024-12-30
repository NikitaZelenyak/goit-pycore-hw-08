def get_upcoming_birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays in the next 7 days."
    
    results = "Upcoming Birthdays:\n"
    for entry in upcoming_birthdays:
        results += f"{entry['name']}: {entry['birthday']}\n"
    
    return results
