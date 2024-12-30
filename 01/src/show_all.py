def show_all(book):
    if not book.records:
        return "No contacts available."
    return "\n".join([str(record) for record in book.records])
  
    
