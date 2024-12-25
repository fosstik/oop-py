class Singleton:
    __instance = None
    
    def __init__(self, test):
        self.test = test

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: 
            cls.__instance = super().__new__(cls)
            return cls.__instance

class OnlyFive: 
    counter = 0
    last_object = None

    def __init__(self):
        OnlyFive.counter += 1  
        if OnlyFive.counter == 5:
            OnlyFive.last_object = self 

    def __new__(cls, *args, **kwargs):
        if OnlyFive.counter < 5:
            return super().__new__(cls)
        else: 
            return cls.last_object


class Book: 
    title = None
    author = None
    year = None 
    data = []

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.data.append(self)

    def __new__(cls, *args, **kwargs):
        for item in Book.data:
            if item.title == args[0] and item.author == args[1]:
                return item
        
        return super().__new__(cls)
