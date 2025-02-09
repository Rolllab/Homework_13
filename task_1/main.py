import json
import math
import random
import threading

"""

Сделал сразу файл. Я могу конечно сделать и как в задании написано, но только вам же его руками вводить.
В общем это не нужно...))

"""

# Входные данные
FILE_PATH = 'file.json'
a, b = 1, 100


def get_random_number() -> list:
    """ Возвращает рандомный список """
    return [random.randint(a, b) for _ in range(10)]


def get_natural_number(x_list) -> list:
    """Возвращает список натуральных (простых) чисел из входного списка."""
    n_list = []
    for x in x_list:
        for item in range(2, (x//2)+1):
            if x % item == 0:
                break
        else:
            n_list.append(x)
    return n_list


def get_factorial(x_list) -> list:
    """Возвращает список факториалов чисел из входного списка."""
    return [math.factorial(x) for x in x_list]



if __name__ == '__main__':
    random_list = get_random_number()
    natural_list = get_natural_number(random_list[:])   # Прочитал, что лучше (в потоки) передавать копию списка
    factorial_list = get_factorial(random_list[:])      # Прочитал, что лучше (в потоки) передавать копию списка

    thread1 = threading.Thread(target=get_random_number, )
    print('-' * 50)
    print('Создан поток 1 для генерации случайных чисел')
    thread1.start()
    print('Запущен поток 1 и заполнил список случайными числами')
    thread1.join()
    print('Поток 1 завершил свою работу')
    print('-' * 50)

    thread2 = threading.Thread(target=get_natural_number, args=[random_list])
    thread3 = threading.Thread(target=get_factorial, args=[random_list])
    print('Созданы еще 2 потока для нахождения натурального числа и вычисления факториала из списка')
    thread2.start()
    thread3.start()
    print('Оба потока успешно стартовали... И нашли натуральные числа и вычислили факториал')
    thread2.join(), thread3.join()
    print('Оба потока закончили свою работу')

    print('-' * 50)
    obj = {
        "Рандомные числа": random_list,
        "Натуральные числа": natural_list,
        "Факториал числа": factorial_list
    }
    print('Создался промежуточный словарь, который ляжет в основу json-файла')
    print('-' * 50)

    with open(FILE_PATH, 'w', encoding='utf-8') as fp:
        json.dump(obj=obj, fp=fp, ensure_ascii=False, indent=4)

    print('Промежуточный объект записан в файл - file.json')
