# Задание 4
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов(n) вводится с клавиатуры.

n = int(input("Введите натуральное число: "))
summa = 0
element = 1
for p in range(n):
    summa += element
    element = element / (-2)

print(summa)