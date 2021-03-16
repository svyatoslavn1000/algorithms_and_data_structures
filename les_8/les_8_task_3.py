# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random

def create_graph(vertex, num_edges):

    graph = {}

    for i in range(vertex):
        graph[i] = set()

        num_edge = random.randrange(1, num_edges)
        while len(graph[i]) < num_edge:
            edge = random.randrange(0, vertex)
            if edge != i:
                graph[i].add(edge)

    return(graph)

def deep(graph, start):
    path = []

    parent = [None]*len(graph)
    is_visited = [False]*len(graph)
    def deep_search(vertex):
        is_visited[vertex] = True
        path.append(vertex)

        for i in graph[vertex]:
            if not is_visited[i]:
                parent[i] = vertex
                deep_search(i)
                path.append(vertex)

        else:
            path.append(-vertex)

    deep_search(start)

    return parent, path

v = int(input("Сколько будет вершин в графе: "))
while True:
    ed = int(input("укажите максимальное число ребер у вершины: "))
    if ed > v:
        print("Число ребер, исходящих из вершины должно быть меньше числа вершин.")
    else:
        break

g = create_graph(v, ed)

for key, value in g.items():
    print(f"Из вершины {key} ребра ведут в вершины {value}")

s = int(input("\n С какой вершины начать обход: "))

parent, path = deep(g, s)
print(parent)

for i, vertex in enumerate(path):
     if i % 10 == 0:
        print()
     if vertex >= 0:
        print(f"{vertex} -> ", end=" ")