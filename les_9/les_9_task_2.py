# 2. Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter
from collections import namedtuple

# collections.Counter - вид словаря,
# который позволяет нам считать количество неизменяемых
# объектов (в большинстве случаев, строк).

# Класс, сохраняющий структуру дерева:
class Node (namedtuple("Node",["left","right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")



class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

#          Кодировщик
def huffman_encode(s : str):
    h = []

    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1

    code = {}

    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")

    return code

# Декодер

def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break

    return "".join(sx)


def main():
    s = input("Веедите строку: ")
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)

    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{} : {}".format(ch, code[ch]))
    print(encoded)
    print(huffman_decode(encoded, code))

main()