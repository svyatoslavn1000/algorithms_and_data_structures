# Задание 3.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = int(input("Введите натуральное число: "))
reverced = 0
while num > 0:
    reverced = reverced * 10 + num % 10
    num = num // 10

print(reverced)