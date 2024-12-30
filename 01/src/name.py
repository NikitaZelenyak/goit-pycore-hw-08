from field import Field
class Name(Field):
    def __init__(self, value):
           if len(value) <= 0:
                  print("Add name")
                  return
           else:
                super().__init__(value)