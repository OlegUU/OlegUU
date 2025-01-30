# Задача "Банковские операции":
# Необходимо создать класс Bank со следующими свойствами:
# Исходный код:
from random import randint
from time import sleep
import threading


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            _sum = randint(50, 500)
            with threading.Lock():
                self.balance += _sum
                print(f'Пополнение: {_sum}. Баланс: {self.balance}')
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            _sum = randint(50, 500)
            print(f'Запрос на {_sum}')
            with threading.Lock():
                if _sum <= self.balance:
                    self.balance -= _sum
                    print(f'Снятие: {_sum}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостаточно средств!')
                    self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


# Вывод на консоль (может отличаться значениями, логика должна быть та же):
# Пополнение: 241. Баланс: 241
# Запрос на 174
# Снятие: 174. Баланс: 67
# Пополнение: 226. Баланс: 293
# Запрос на 421
# Запрос отклонён, недостаточно средств
# Пополнение: 133. Баланс: 426
# Запрос на 422
# Снятие: 422. Баланс: 4
# Пополнение: 150. Баланс: 154
# Запрос на 207
# Запрос отклонён, недостаточно средств
# ....
# Запрос на 431
# Снятие: 431. Баланс: 276
# Запрос на 288
# Запрос отклонён, недостаточно средств
# Итоговый баланс: 276
#
# Примечания:
# Для генерации случайного целого числа используйте функцию randint из модуля random.
# Для ожидания используйте функцию sleep из модуля time.
# Особо важно соблюсти верную блокировку: в take замок закрывается, в deposit открывается.