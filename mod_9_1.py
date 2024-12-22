# Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.
# Задача "Вызов разом":

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results.update({func.__name__: func(int_list)})
    return results

# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# Вывод на консоль:
# {'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
