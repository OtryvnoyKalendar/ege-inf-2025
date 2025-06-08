from functools import *

@lru_cache(maxsize = 10_000) # 130МБ ОЗУ
# @lru_cache(None) # 300МБ ОЗУ
def f(n):
    if n < 20:
        return n
    else:
        return (n-6) * f(n - 7)

for i in range(19, 47_880):
    f(i)

# input() если сами хотите проверить затраты памяти 

res = (f(47_872) - 290 * f(47_865)) // f(47_858)
print(res)
