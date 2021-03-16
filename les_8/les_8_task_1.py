# 1. На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?



def meeting(num):
    if num < 1:
        print("Надо больше друзей")

    handshakes = []

    for i in range(num):
        for j in range(i):
                handshakes.append([i,j])

    return handshakes

friends = meeting(int(input("Введите число друзей: ")))
print(friends)
print(len(friends))
