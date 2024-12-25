import re
from string import ascii_lowercase, digits

class CardCheck: 
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.match(pattern, number))

    @classmethod
    def check_name(cls, name):
        words = name.split()
        if len(words) != 2:
            return False
        
        first_name, last_name = words
        return all(char in cls.CHARS_FOR_NAME for char in first_name) and (char in cls.CHARS_FOR_NAME for char in last_name)


class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32
    
    @classmethod
    def from_kelvin(cls, kelvin):
        cls.celsius = kelvin - 273.15
        return super().__new__(cls)
    


class Employee:
    name = None
    age = None
    post = None

    @staticmethod
    def is_valid_age(age):
        return age >= 18 or age <= 65
    
    @classmethod 
    def from_string(cls, string: str):
        data = string.split(', ')
        if Employee.is_valid_age(int(data[1])):
            cls.name = data[0]
            cls.age = int(data[1])
            cls.post = data[2]
            return super().__new__(cls)
        else:
            raise ValueError('Ощибка')
        
    def get_details(self):
        return f'имя:{self.name}\nвозраст:{self.age}\nдолжность:{self.post}\n'
        
a = Employee.from_string('Илья, 12, Да')
    
print(a.get_details())




    