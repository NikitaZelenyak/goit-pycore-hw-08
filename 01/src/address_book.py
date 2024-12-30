from datetime import datetime, timedelta
from collections import UserDict
class AddressBook(UserDict):
    def __init__(self):
                super().__init__() 
                self.records = []
    def add_record(self, record):
                self.records.append(record)
    def find(self, name):
                for record in self.records:
                    if record.name.value == name:
                         return record
    def delete(self, name):
                 for record in self.records:
                      if record.name.value == name:
                           self.records.remove(record)
                           return
    def get_upcoming_birthdays(self):
        current_date = datetime.today().date()
        end_date = current_date + timedelta(days=7)
        pattern = "%Y-%m-%d"

        upcoming_birthdays = []
        for record in self.records:
            if record.birthday:
                birthday_this_year = record.birthday.value.date().replace(year=current_date.year)
                if birthday_this_year < current_date:
                    birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

                if current_date <= birthday_this_year <= end_date:
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime(pattern),
                    })
        return upcoming_birthdays



                      