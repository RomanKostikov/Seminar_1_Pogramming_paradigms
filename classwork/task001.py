# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.
# Задача
# Реализовать императивную функцию поиска элементов на языке Python.

import random


def search_imp(target, array):
    for num in array:
        if num == target:
            return True
    return False


array = []
for i in range(10):
    array.append(random.randint(-10, 10))
print(array)

print(search_imp(5, array))
