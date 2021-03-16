# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

def counter_substring(string: str):

    hash_dict = {}

    for i in range(len(string) - 1):
        for j in range(i+1, len(string)+1):
            hash_dict[hash(string[i:j])] = string[i:j]

    return hash_dict

my_str = input("Введите строку:  ")
print(counter_substring(my_str))
count = len(counter_substring(my_str))
print(f"В строке {my_str} содержится {count} различных подстрокстрок")