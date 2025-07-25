"""
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 1 при n = 1;
F(n) = 2 n F(n − 1), если n > 1.

Чему равно значение выражения (F(2024) −  F(2023)) / F(2022)?
"""

# можно и другими способами кншн
# этот вариант решения занимает в памяти те же (я неправильно посчитал)МБ. Вывод - по памяти нет разницы lru_cache или setrecursionlimit
from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n - 1)

for n in range(2026):
    f(n)

res = (f(2024) - f(2023)) / f(2022)
print(int(res))
# 16374162
