# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
# Пример процедуры для сортировки списка чисел в порядке убывания, используя алгоритм сортировки выбором:

from random import randint
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError(
            'На вход должен подаваться непустой целочисленный список')
    return sorted(arr, reverse=True)


numbers = [randint(0, 100) for i in range(7)]
print(numbers)
print(bubble_sort(numbers))
