from itertools import *

tab = "24567 146 5 12 1367 125 15".split()
pic = "аб бв бе бж вж гж гд де же".split()

print(*range(1, 8))

for p in permutations("абвгдже"):
    if all(str(p.index(b) + 1) in tab[p.index(a)] for a, b in pic):
        print(*p)

"""
1 2 3 4 5 6 7
ж д а г б е в
=> д->е => 2->6 = 25
"""
