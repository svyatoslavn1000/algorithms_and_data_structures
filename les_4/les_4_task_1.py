#Задача: простым суммированием найти сумму членов последовательности
#В Debian все рецепты из лекций не работают.
#Поэтому я пользовался только библиотеками Python, без использования терминала.

import timeit
import cProfile

# def test_geom():
#     lst = [1,3,7,15,31,63,127,255,511,1023,2047]
#     for i, item in enumerate(lst):
#         assert item == summa1(i, 2)
#         print(f'test {i} Ok')



def summa1(n, q):
    sum = 1
    element = q
    for p in range(n):
        sum += element
        element = element * q
    return sum

start_time = timeit.default_timer()
for i in range(1000):
    summa1(1, 1000)
time_1 = timeit.default_timer() - start_time
print('summa 1 took', time_1)


cProfile.run(summa1(1000, 2))

# summa 1 took 0.0010055110324174166
#          2 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}