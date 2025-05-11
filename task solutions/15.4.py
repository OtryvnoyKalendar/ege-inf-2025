from itertools import *

def f(x, a1, a2):
    p = 5 <= x <= 30
    q = 14 <= x <= 23 
    a = a1 <= x <= a2

    return (p == q) <= (not a)

ox = [i/4 for i in range(5*4, 31*4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(f(x, a1, a2) == True for x in ox):
        res.append(a2 - a1)

print(max(res))
