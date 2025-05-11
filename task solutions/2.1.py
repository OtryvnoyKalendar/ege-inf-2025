print("x y z w")


def f(x, y, z, w):
    return (not x and not y) or (y == z) or w


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w) == 0:
                    print(x, y, z, w)

"""
смотрим и анализируем
x y z w
0 1 0 0
1 0 1 0
1 1 0 0
"""

"""
ответ: zwyx
"""

"""
У разных заданий меняется только функция
"""
