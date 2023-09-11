# ● Условие
# На вход подается: список целых чисел arr
# ● Задача
# Реализовать декларативную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел

import random


# def doli_decl(array: list[int]) -> tuple[float]:
#     if len(array) == 0:
#         raise ValueError('Required not empty list.')
#     pos = list(filter(lambda x: (x > 0), array))
#     nul = list(filter(lambda x: x == 0, array))
#     neg = list(filter(lambda x: x < 0, array))
#     return len(pos) / len(array), len(nul) / len(array), len(neg) / len(array)

def nums_share_decl(arr):
    size = len(arr)
    list0 = list(filter(lambda num: num == 0, arr))
    list_pos = list(filter(lambda num: num > 0, arr))
    list_neg = list(filter(lambda num: num < 0, arr))
    return len(list0) / size, len(list_pos) / size, len(list_neg) / size


array = []
for i in range(10):
    array.append(random.randint(-10, 10))
print(array)

print(nums_share_decl(array))
