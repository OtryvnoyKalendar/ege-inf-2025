"""
На числовой прямой даны два отрезка: `P = [17; 54]` и `Q = [37; 83]`. Укажите наименьшую возможную длину такого отрезка A, что логическое выражение  
```
(x ∈ P) → (((x ∈ Q) and ¬(x ∈ A)) → ¬(x ∈ P))
```
истинно (т.е. принимает значение 1) при любом значении переменной х.
"""

# это плохой пример
diff = 0 # иногда нужно поставить 0.5
table = [x for y in (17, 37, 54, 83) for x in (y, y+diff, y-diff)]

def f(x, a1, a2):
    p = 17 <= x <= 54
    q = 83 <= x <= 37
    a = a1 <= x <= a2

    return (p) <= (((q) and (not (a))) <= (not (p)))

res = []
for a1 in table:
    for a2 in table:
        if a2 > a1 and all(f(x, a1, a2) == True for x in table):
                res.append(a2 - a1)

print(min(res))
# Ответ: 17

# решение основано на решении Владимирова Дмитрия
mn=999999

def f2(x, a1, a2):
    return ( 17 < x < 54) <= (((37 < x< 83) and not( a1 < x < a2)) <= (not(17< x < 54)))

for a1 in range(1,100):
    for a2 in range(1,100):
        if all(f2(x, a1, a2) for x in range (1,100)):
            mn = min(mn, a2-a1)

print(mn)
