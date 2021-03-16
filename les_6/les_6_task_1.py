# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков. П
# роанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить
# в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

# from collections import Mapping, Container
import sys
import collections

class Test_memory:
    def __init__(self):
        self.memory = 0
        self.objects = {}

    def put_obj(self, *args):
        for o in args:
            self.append_values(o)

    def append_values(self, object):
        value = sys.getsizeof(object)
        name_same_obj = str(object.__class__)
        self.memory += value
        if name_same_obj in self.objects:
            self.objects[name_same_obj][0] += 1
            self.objects[name_same_obj][1] += sys.getsizeof(object)
        else:
            self.objects[name_same_obj] = [1]*2
            self.objects[name_same_obj][1] = sys.getsizeof(object)



    def print_all(self):
        print(f'Объекты заняли всего {self.memory} байт')
        for key, value in self.objects.items():
            print(f'Объекты класса {key} числом {value[0]} заняли {value[1]} байт')

