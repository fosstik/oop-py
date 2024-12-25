from datetime import datetime

class Book:
    def __init__(self,title, author,pages):
        self.title = title 
        self._author = author
        self.__pages = pages

    def get_author(self): 
        return self._author

    def set_author(self, author):
        self._author = author

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Кол-во страниц должно быть положительным.")

    def display_info(self):
        return f"Название: `{self.title}`, Автор: {self._author}, Страниц: {self.__pages}"



class Car:
    def __init__(self,model, year,mileage):
        self.model = model
        self._year = year
        self.__mileage = mileage

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self._year

    def set_model(self, year):
        if year > 1886 <= datetime.now().year:
            self._year = year
        else:
            raise ValueError("Год выпуска автомобиля не должен быть раньше 1886 ")
    
    def get_mileage(self):
        return self.__mileage
    
    def set_model(self, mileage):
        if mileage > 0:
            self.__mileage = mileage
        else:
            raise ValueError("Пробег не может быть отрицательным")
        

