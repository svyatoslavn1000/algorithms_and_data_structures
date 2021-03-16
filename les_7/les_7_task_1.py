# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

def sorted_by_bubble(array, ask = 1):

    position = 1

    while position < len(array):
        is_sorted = True

        for i in range(len(array) - position):
            if array[i] * ask < array[i + 1] * ask:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        position += 1

size = 100
minimax = 100
data = [random.randrange(-minimax , minimax ) for i in range(size)]
print(data)
sorted_by_bubble(data, ask = 1)
print(data)