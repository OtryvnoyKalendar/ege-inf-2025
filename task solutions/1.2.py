# решение Данила Шарлова
from itertools import permutations

table = '568 36 247 368 178 124 35 145'.split()
graph = {
    'А': ['Б', 'Г', 'Ж'],
    'Б': ['А', 'Г', 'Е'],
    'В': ['Г', 'Е', 'Д'],
    'Г': ['А', 'Б', 'В'],
    'Д': ['В', 'К', 'Ж'],
    'Е': ['Б', 'В', 'К'],
    'Ж': ['А', 'Д'],
    'К': ['Е', 'Д']
}

print(*range(1, 9))

for perm in permutations(graph.keys()):
    indices = {node: str(i + 1) for i, node in enumerate(perm)}
    if all(len(graph[node]) == len(table[i]) for i, node in enumerate(perm)) and all(indices[neighbor] in table[i] for i, node in enumerate(perm) for neighbor in graph[node]):
        print(' '.join(perm))
        break

"""
1 2 3 4 5 6 7 8
Б К Д В А Е Ж Г
=> бв = 14
"""
