# ● Условие
# На вход подается: список целых чисел arr
# ● Задача
# Реализовать императивную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел
import random


def nums_share_imp(arr):
    count_zero = 0
    count_pos = 0
    count_neg = 0
    for num in arr:
        if num == 0:
            count_zero += 1
        elif num > 0:
            count_pos += 1
        else:
            count_neg += 1

    return "zeros share = " + str(count_zero / len(arr)), "positive numbers share = " + str(
        count_pos / len(arr)), "negative numbers share = " + str(count_neg / len(arr))


array = []
for i in range(10):
    array.append(random.randint(-10, 10))
print(array)

print(nums_share_imp(array))
