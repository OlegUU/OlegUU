# Цель: научиться создавать классы наследованные от класса Thread.
#
# Задача "За честь и отвагу!":

from threading import Thread
from time import sleep


class Knight(Thread):  # Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
    def __init__(self, name_,power):
        super().__init__()  # Инициализация родительского класса Thread
        self.name_= str(name_)  # Атрибут name - имя рыцаря. (str)
        self.power= int(power)  # Атрибут power - сила рыцаря. (int)

    def run(self):  # А также метод run, в котором рыцарь будет сражаться с врагами:
        print(f'{self.name_}, на нас напали!')  # При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
        num_days= 0
        enemies= 100  # Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).

        while enemies >0:  # В процессе сражения количество врагов уменьшается на power текущего рыцаря.
            sleep(1)
            num_days += 1
            enemies -= self.power
            if enemies < 0:
                enemies= 0
            print(f'{self.name_}, сражается {num_days} день(дня)..., осталось {enemies} воинов.')
        print(f'{self.name_} одержал победу спустя {num_days} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")

