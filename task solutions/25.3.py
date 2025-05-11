from fnmatch import *

k = 0
for i in range(0, 10**9, 7):
    if fnmatch(str(i), '?3579?6*'):
        k+=1

print(k)
