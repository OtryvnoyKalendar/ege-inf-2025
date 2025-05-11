from itertools import *

tab = '568 36 247 368 178 124 35 145'.split()
pic = 'аг аб аж бг бе вг ве вд дж дк ек'.split()
print(*range(1,9))

for p in permutations('абвгдежк'):
    if all(str(p.index(b) + 1) in tab[p.index(a)] for a, b in pic):
        print(*p)

"""
1 2 3 4 5 6 7 8
б к д в а е ж г
=> бв = 14
"""
