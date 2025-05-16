# s - колво камней, n - за сколько ходов закончится игра
def f(s, n):
    he = n % 2 == 0
    if s >= 36:
        return he
    if n == 0:
        return False

    table = [
        f(s + 2, n - 1),
        f(s * 3, n - 1),
    ]

    if he:
        return all(table)
    else:
        return any(table)

res = [s for s in range(1, 36) if f(s, 1)]
print("19.", min(res), res)
res = [s for s in range(1, 36) if not f(s, 1) and f(s, 3)]
print("20.", *res)
res = [s for s in range(1, 36) if not f(s, 2) and f(s, 4)]
print("21.", *res)

"""
Ответы:
12
89
67
"""

"""
19) Можно применить простое рассуждение:
Чтобы Петя победил своим первым ходом, он должен увеличить количество камней в куче на столько, чтобы их стало больше или равно 36. Эффективнее Пете будет утраивать S, чем добавлять к нему 2. При каких S будет выполняться 3 ⋅S >= 36  ? При S ≥ 12. Следовательно ответ 12.
"""
