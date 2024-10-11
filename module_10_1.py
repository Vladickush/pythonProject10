# Задача "Потоковая запись в файлы":
import time
from _datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    file = open(file_name, 'w')
    for count in range(word_count):
        file.write('Какое-то слово № ' + str(count + 1) + '\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    file.close()


# Обычный вызов
start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish = datetime.now()
print(f'Работа потоков {finish - start}')

# Потоковый вызов
start = datetime.now()
first = Thread(target=write_words, args=(10, 'example5.txt'))
second = Thread(target=write_words, args=(30, 'example6.txt'))
third = Thread(target=write_words, args=(200, 'example7.txt'))
fourth = Thread(target=write_words, args=(100, 'example8.txt'))

first.start()
second.start()
third.start()
fourth.start()

first.join()
second.join()
third.join()
fourth.join()

finish = datetime.now()
print(f'Работа потоков {finish - start}')
