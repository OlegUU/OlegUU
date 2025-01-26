# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
# Задача "Функциональное разнообразие":
# Lambda-функция:
# Даны 2 строки:
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

my_lambda = list(map(lambda x, y: x == y, first, second))
print(my_lambda)
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.
def get_advanced_writer(file_name ):
    def write_everything(*data_set):
        with open(file_name , mode='w', encoding='utf-8') as file:
            for data in data_set:
                file.write(f'{data}\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
      return choice(self.words)

# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное

