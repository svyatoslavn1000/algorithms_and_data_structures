# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

dim = 20
interval = 10
arr = [random.randint(-interval, interval) for _ in range(dim)]

ind_min = 0
ind_max = 0

for p in range(dim):
    if arr[p] < arr[ind_min]:
        ind_min = p
    elif arr[p] > arr[ind_max]:
        ind_max = p

print(arr)
arr[ind_min], arr[ind_max] = arr[ind_max], arr[ind_min]
print(arr)