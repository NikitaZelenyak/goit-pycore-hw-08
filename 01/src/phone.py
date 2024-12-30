from field import Field
class Phone(Field):
      def __init__(self, value):
            if len(value) == 10:
                  super().__init__(value)
            else:
                  print("Phone must contain 10 symbols")