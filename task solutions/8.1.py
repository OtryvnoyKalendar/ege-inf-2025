from itertools import *

c = 1

for i in product("ЩОГБА", repeat=6):
    s = "".join(i)
    if s == "ОБЩАГА":
        print(c, s)
    c += 1

"""
5115 ОБЩАГА
"""
