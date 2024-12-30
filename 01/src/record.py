from name import Name
from phone import Phone
from birthday import Birthday
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None    

    def add_phone(self, phone):
          self.phones.append(Phone(phone))

    def find_phone(self, phone):
          for number in self.phones:
                if number.value == phone:
                      return number
                
    def edit_phone(self, phone, new_phone):
          for index in range(len(self.phones)):
                if self.phones[index] == phone:
                      self.phones[index]= new_phone
                      
                
    def remove_phone(self, phone):
          self.phones.remove(phone.value)

    def add_birthday(self, value):
         self.birthday = (Birthday(value))
     


    

    def __str__(self):
       return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"