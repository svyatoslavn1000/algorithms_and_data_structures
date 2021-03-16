# 3. Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.


import random
import statistics

def quickselect_median(incoming_list, pivot_fn = random.choice):
    if len(incoming_list) % 2 == 1:
        return quickselect(incoming_list, len(incoming_list) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(incoming_list, len(incoming_list) / 2 - 1, pivot_fn) +
                      quickselect(incoming_list, len(incoming_list) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    if len(l) == 1:
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)



size = 13
n = 5
minimax = 2 * n + 1
data = [random.randrange(0 , minimax ) for i in range(size)]
print(data)

# Решение нашел на Хабре. Работает для любых массивов. https://habr.com/ru/post/346930/
# Алгоритм классический, так что не вижу смысла делать свой велосипед. Работает для массивов любого размера.
print(quickselect_median(data))

# решение из коробки
print(statistics.median(data))