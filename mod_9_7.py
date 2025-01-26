# Задание: Декораторы в Python
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
def is_prime(func):
    def wrapper(*args):
        result=func(*args)
        div = 2
        while div <result and result % div != 0:
            div += 1
        if div == result:
            print('Простое')
        else:
            print('Состовное')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример:
result = sum_three(2, 3, 6)
print(result)
# Результат консоли:
# Простое
# 11
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three
# Успехов!