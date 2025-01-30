import threading
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time =datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time=datetime.now()
print(f"Работа потоков {end_time-start_time}")

start_time_threads= datetime.now()

threads= []
threads.append(threading.Thread(target=write_words,args=(10,'example5.txt')))
threads.append(threading.Thread(target=write_words,args=(30,'example6.txt')))
threads.append(threading.Thread(target=write_words,args=(200,'example7.txt')))
threads.append(threading.Thread(target=write_words,args=(100,'example8.txt')))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = datetime.now()
print(f"Работа потоков {end_time_threads-start_time_threads}")

# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время
