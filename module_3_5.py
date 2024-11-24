def get_multiplied_digits(number): # Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.
    str_number=str(number) # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    first = int(str_number[0])# Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


# Исходный код:
#
result = get_multiplied_digits(40203)

print(result)

# Вывод на консоль:
#
# 24

