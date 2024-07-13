import threading
import random


def get_list():
    global lst
    lst = [random.randint(1, 10) for _ in range(100)]
    print(lst)


t1 = threading.Thread(target=get_list)
t1.start()
t1.join()


def get_sum():
    sum_result = sum(lst)
    print("Сумма элементов списка:", sum_result)


def get_mean():
    mean_result = sum(lst) / len(lst)
    print("Среднее арифметическое элементов списка:", mean_result)


t2 = threading.Thread(target=get_sum)
t3 = threading.Thread(target=get_mean)

t2.start()
t3.start()

t2.join()
t3.join()
# использовала глобальную переменную, потому что через args выдает ошибку, ну и с global удобнее
