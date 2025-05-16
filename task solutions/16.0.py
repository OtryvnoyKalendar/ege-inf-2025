from functools import *

@lru_cache
def f(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n - 1) - 2*g(n-1)

@lru_cache
def g(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n - 1) + g(n-1) + n

res = sum([int(x) for x in str(g(36))])
print(res) # 40
