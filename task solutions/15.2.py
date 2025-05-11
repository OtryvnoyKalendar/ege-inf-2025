"""
Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n. Так, например,
14 & 5 = 11102 & 01012 = 01002 = 4.

Для какого наименьшего неотрицательного целого числа А формула
```
((x & 42 ≠ 0) and (x & 34 = 0)) → ¬ (x & А = 0)
```
тождественно истинна (т.е. принимает значение 1) при любом неотрицательном целом значении переменной х?
"""

# так
def f(A, x, y):
    return ((x & 42 != 0) and (x & 34 == 0)) <= (not (x & A == 0))

range_a = range(0, 200)
range_other = range(1, 100)
for A in range_a:
    table = (f(A, x, y) == True for x in range_other for y in range_other) # кортеж
    if all(table):
        print(A)
        break

# флагами
for A in range(0,1000):
    b=True
    for x in range(0,1000):
        if (((x&42!=0)and(x&34==0))<=(not(x&A==0)))==False:
            b=False
            break
    if(b):
        print(A)
        break

# Ответ: 8
