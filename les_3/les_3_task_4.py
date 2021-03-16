# 4. Определить, какое число в массиве встречается чаще всего.

import random

dim = 10
interval = 20
arr = [random.randint(0, interval) for _ in range(dim)]

number = arr[0]
max_frequency = 1

for p in range(dim -1):
    frequency = 1
    for q in range(p+1, dim):
        if arr[p] == arr[q]:
            frequency +=1
    if frequency > max_frequency:
        max_frequency = frequency
        number = arr[p]
print(arr)
if max_frequency > 1:
    print(f"В массиве чаще всего встресчается {number}, всего {max_frequency} раз.")
else:
    print("Все числа в массиве встречаются один раз.")