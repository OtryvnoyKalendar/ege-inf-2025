def f(s, a, n):
    he = n % 2 == 0
    if s + a >= 69:
        return he
    if n == 0:
        return False

    table = [
        f(s+2, a, n-1),
        f(s*2, a, n-1),
        f(s, a+2, n-1),
        f(s, a*2, n-1),
    ]
    
    if he:
        # если в 19 номере Петя сделал неудачный ход, то меняем all -> any (ДЛЯ 20 и 21 ВОЗВРАЩАЕМ ВСЕ НА СВОИ МЕСТА)
        return all(table)
    else:
        return any(table)

print(19, [s for s in range(1, 60) if f(s, 9, 2)])
print(20, [s for s in range(1, 60) if not f(s, 9, 1) and f(s, 9, 3)])
print(21, [s for s in range(1, 60) if not f(s, 9, 2) and f(s, 9, 4)])

"""
На выходе:
19 [29]
20 [25, 27, 28]
21 [23, 26]
"""
