# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.
# Задача
# Реализовать декларативную функцию поиска элементов на языке Python.

# def search_declarative(array, target):
#     return target in array

def search_decl(target, array, i=0, count=0):
    if i >= len(array):
        return count
    tmp = 0
    if isinstance(array[i], list):
        tmp = search_decl(target, array[i], i=0, count=0)
    if array[i] == target:
        count += 1
    return search_decl(target, array, i=i+1, count=count + tmp)