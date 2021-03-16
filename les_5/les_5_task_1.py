# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

def otchot():
    num_periods = 4
    Corporation = namedtuple('Corporation', ['name_corp', 'quartals', 'profit_corp'])
    all_corprporations = []
    total_profit = 0

    count = int(input("Введите число предприятий: "))
    for i in range(1, count + 1):
        profit = 0
        quartals = []
        name = input(f'Введите название {i} - го предприятия: ')

        for j in range(num_periods):
            quartals.append(int(input(f"Прибыль за {j + 1} квартал: ")))
            profit += quartals[j]

        corporation = Corporation(name_corp=name, quartals=tuple(quartals), profit_corp=profit)
        all_corprporations.append(corporation)
        total_profit += profit

    average = total_profit / count

    print(f"Средняя прибыль = {average} ")

    print(f"Предприятия с прибылью выше среднего: ")
    for corporation in all_corprporations:
        if corporation.profit_corp > average:
            print(f"Предприятие {corporation.name_corp} получило прибыль {corporation.profit_corp}")
            for i in range(num_periods):
                print(f"В том числе за {i + 1} - й квартал: {corporation.quartals[i]}")

    print(f"Предприятия с прибылью ниже или равной средней: ")
    for corporation in all_corprporations:
        if corporation.profit_corp <= average:
            print(f"Предприятие {corporation.name_corp} получило прибыль {corporation.profit_corp}")
            for i in range(num_periods):
                print(f"В том числе за {i + 1} - й квартал: {corporation.quartals[i]}")


otchot()
