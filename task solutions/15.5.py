'''
На числовой прямой даны два отрезка: `D = [17; 58]` и `C = [29; 80]`. Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение
```
(x ∈ D) → ((¬(x ∈ C)∧ ¬(x ∈ A)) → ¬(x ∈ D))
```
истинно (то есть принимает значение 1) при любом значении переменной х.
'''

diff = 0.5 # тут тоже не особо надо
nums = [y for x in [17, 29, 58, 80] for y in (x, x+diff, x-diff)]

def f(x, a1, a2):
    d = 17 <= x <= 58
    c = 29 <= x <= 80
    a = a1 <= x <= a2 
    return (d) <= (((not(c)) and (not(a))) <= (not(d)))

res = []
for a1 in nums:
    for a2 in nums:
        if a2 > a1:
            if all(f(x, a1, a2) == True for x in nums):
                res.append(a2 - a1)

print(round(min(res)))
# ответ: 12
