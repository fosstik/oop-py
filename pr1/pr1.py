class Human:
    height = None 
    age = None

human_one = Human()
human_two = Human()

print(human_one.age)
print(human_two.age)

human_one.age = 22
human_two.age = 27

print(human_one.age)
print(human_two.age)

delattr(human_one, 'height')
delattr(human_two, 'height')

print(hasattr(human_one, 'height'))
print(hasattr(human_two, 'height'))


class Goods: 
    title = "Мороженное"
    weight = 151
    type = "Еда"
    price = 12321

goods_one = Goods()

goods_one.weight = 4
goods_one.price = 500 

print(goods_one.weight)
print(goods_one.price)

class Car:
    ...
    
new_car = Car()

new_car.model = "Тойота"
new_car.color = "Чёрный"
new_car.number = "П34А123"

print(new_car.model)
print(new_car.color)
print(new_car.number)
