import random
import threading

# Глобальная блокировка для синхронизации вывода
lock = threading.Lock()


def get_random_number(a=1, b=100) -> list:
    """ Возвращает рандомный список """
    return [random.randint(a, b) for _ in range(10)]


def get_sum_list(iterator):
    """Получаем сумму элементов входного списка."""
    for i in range(5):
        sum_list = sum(iterator)
        with lock:  # Получаем блокировку перед выводом
            print(f"Поток SUM:  Итерация {i + 1}: Сумма элементов списка = {sum_list}")


def get_arithmetic_mean(iterator):
    """Получаем среднеарифметическое значение элементов входного списка."""
    for i in range(5):
        arithmetic_mean = sum(iterator)/len(iterator)
        with lock:
            print(f"Поток ARITHMETICS MEAN:  Итерация {i+1}: Среднеарифметическое в списке = {arithmetic_mean}")


if __name__ == '__main__':
    random_list = get_random_number()
    print(f"Исходный (рандомный) список: {random_list[:]}")

    thread1 = threading.Thread(target=get_sum_list, args=[random_list[:]])
    thread2 = threading.Thread(target=get_arithmetic_mean, args=[random_list[:]])


    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
