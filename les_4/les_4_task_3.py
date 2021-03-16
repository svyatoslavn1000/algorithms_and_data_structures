import timeit
import cProfile

# def test_geom():
#     lst = [1,3,7,15,31,63,127,255,511,1023,2047]
#     for i, item in enumerate(lst):
#         assert item == summa2(i, 2)
#         print(f'test {i} Ok')



def summa2(n, q):
    if n == 0:
        return 1
    return summa2(n-1, q) + q ** (n )


start_time = timeit.default_timer()
for i in range(1000):
    summa2(1, 1000)
time_1 = timeit.default_timer() - start_time
print('summa 2 took', time_1)


cProfile.run(summa2(100,2))
#
# summa 2 took 0.001355538028292358
#          2 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


