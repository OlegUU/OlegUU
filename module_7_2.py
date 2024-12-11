# Цель: Закрепить знания о позиционировании в файле, использовав метод tell()
#    файлового объекта. Написать усовершенствованную функцию записи.
#
# Задача "Записать и запомнить":

def custom_write(file_name, strings): #Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
        for index, string in enumerate(strings):
            byte_start = file.tell()
            file.write(string + '\n')
            strings_positions[(index + 1, byte_start)] = string

    return strings_positions #Возвращать словарь strings_positions

# Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
#
# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')