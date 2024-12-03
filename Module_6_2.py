class Vehicle: # I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner_name, model, color, engine_power):
        self.owner = owner_name # - владелец транспорта. (владелец может меняться)
        self.__model = model # - модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = int(engine_power) # - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)Атрибут
        self.__color = color # - название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model (self): #- возвращает строку: "Модель: <название модели транспорта>"
        return f'Модель: {self.__model}'

    def get_horsepower (self):#- возвращает строку: "Мощность двигателя: <мощность>"
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color (self):   #- возвращает строку: "Цвет: <цвет транспорта>"
        return f'Цвет: {self.__color}'

    def print_info (self): #- распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color (self, new_color): #- принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        if str(new_color).lower() in [c.lower() for c in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print (f'Нельзя сменить цвет на: {new_color}')
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# А так же атрибут класса:
# Взаимосвязь методов и скрытых атрибутов:
# Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами: __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
# Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
# Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
# II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
# Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
#
# Пункты задачи:
# Создайте классы Vehicle и Sedan.
# Напишите соответствующие свойства в обоих классах.
# Не забудьте сделать Sedan наследником класса Vehicle.
# Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.



# Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()
# Вывод на консоль:
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Нельзя сменить цвет на Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok

