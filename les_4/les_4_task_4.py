#Задание 2. Поиск простых чисел без решета Эратосфена.

# import cProfile

def simple(num):
    count = 1
    simple= [2]

    while count < num:
        count += 1
        for i in range(2, int(count ** 0.5) + 1):
            if count % i == 0:
                break
        else:
            simple.append(count)
            count += 1
    return simple
print(type(simple))
print(simple(100))
