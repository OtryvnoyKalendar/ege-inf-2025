from itertools import *

c = 0

for i in permutations("КУСАТЬ", r=5):
    s = "".join(i)
    # if s[0] != "Ь" and s.count("СУК") == 0:
    if s[0] != "Ь" and not "СУК" in s:
        c += 1

print(c)

"""
Ответ: 586
"""
