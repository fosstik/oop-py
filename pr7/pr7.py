class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
    
    @property 
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средства")
        self.balance -= amount

class Product:
    name=None
    _price = None
    _discount = None

    @property 
    def price_with_discount(self):
        return self.price * self.discount / 100
    
    @property
    def price(self):
        return self._price
    
    @property
    def discount(self):
        return self._discount
    
    @price.setter()
    def price(self, price):
        if price <= 0:
            raise ValueError('Цена не может быть меньше 0')
        self._price = price

    @discount.setter()
    def discount(self, discount):
        if 0 >= discount >= 100:
             raise ValueError('Цена не может быть меньше 0% или больше 100%')
        self._discount = discount

class Emoloyee:
    name = None
    _salary = None
    age = None
    
    @property 
    def salary_count(self, salary):
        if salary < 30000:
            raise ValueError('Зарплата не может быть меньше 30000₽')
        self._salary = salary

    @property
    def name(self):
        return self.name
    
    @property
    def age(self):
        return self.age
    
    @age.setter()
    def set_age(self, age):
        self.age = age

    @age.deleter()
    def delete_age(self):
        self.age = None

    @_salary.setter()
    def apply_raise(self, salary):
        return self._salary + salary
    
    