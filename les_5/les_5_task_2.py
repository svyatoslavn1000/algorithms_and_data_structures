# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int()
# для преобразования систем счисления, задача решается в
# несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из
# одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque

HEX_DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def sum_hex(x, y):

    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            res = HEX_DIGITS[x.pop()] + HEX_DIGITS[y.pop()] + transfer

        else:
            res = HEX_DIGITS[x.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(HEX_DIGITS[res])

        else:
            result.appendleft(HEX_DIGITS[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return list(result)


def mult_hex(x, y):

    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = HEX_DIGITS[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * HEX_DIGITS[x[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(HEX_DIGITS[res])

        else:
            result.appendleft(HEX_DIGITS[res % 16])
            transfer = res // 16

    if transfer:
            result.appendleft(HEX_DIGITS[transfer])

    return list(result)

str1 = input('Введите 1-е шестнадцатиричное число: ').upper()
str2 = input('Введите 2-е шестнадцатиричное число: ').upper()

a = list(str1)
b = list(str2)

print(*a, '+', *b, '=', *sum_hex(a, b))

print(*a, '*', *b, '=', *mult_hex(a, b))