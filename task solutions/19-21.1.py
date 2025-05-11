# s - колво камней, n - за сколько ходов закончится игра
def f(s, n):
    he = n % 2 == 0
    if s >= 25:
        return he
    if n == 0:
        return False

    table = [
        f(s + 2, n - 1),
        f(s * 2, n - 1),
    ]

    if he:
        return all(table)
    else:
        return any(table)

print("19. ", [s for s in range(1, 25) if f(s, 2)])
print("20. ", [s for s in range(1, 25) if not f(s, 1) and f(s, 3)])
print("21. ", [s for s in range(1, 25) if not f(s, 2) and f(s, 4)])

"""

"""
