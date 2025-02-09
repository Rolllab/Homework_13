import random
import threading

# Глобальная блокировка для синхронизации вывода
lock = threading.Lock()


def get_random_number(a=1, b=100) -> list:
    """ Возвращает рандомный список """
    return [random.randint(a, b) for _ in range(10)]


def get_max_cont(iterator):
    """Получаем максимальное значение входного списка."""
    for i in range(5):
        max_value = max(iterator)
        with lock:  # Получаем блокировку перед выводом
            print(f"Поток MAX:  Итерация {i + 1}: Максимум = {max_value}")


def get_min_count(iterator):
    """Получаем минимальное значение входного списка."""
    for i in range(5):
        min_value = min(iterator)
        with lock:
            print(f"Поток MIN:  Итерация {i+1}: Минимум = {min_value}")


if __name__ == '__main__':
    random_list = get_random_number()
    print(f"Исходный (рандомный) список: {random_list[:]}")

    thread1 = threading.Thread(target=get_max_cont, args=[random_list[:]])
    thread2 = threading.Thread(target=get_min_count, args=[random_list[:]])


    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
