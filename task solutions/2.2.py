from itertools import *


def f(x, y, z, w):
    return ((not x) and (not y)) or (y == z) or w


for i in product([0, 1], repeat=4):
    table = [
        (i[0], i[1], 1, i[2]),
        (1, 0, i[3], 1),
        (0, 0, 1, 1),
    ]

    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p)


"""
ответ: zwyx
"""

"""
У разных заданий меняется функция(по формуле из условия), repeat(по числу пропусков в таблице), table(по таблице), permutations, соответствие условию(по таблице)

Тут обязательно использовать кортежи иначе будет ошибка TypeError: unhashable type: 'list'
"""
