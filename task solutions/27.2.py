f = open('272A.txt')
n = int(f.readline())
k = int(f.readline())
lst = [int(x) for x in f]
s, m = 0, 0

for i in range(k, n):
    m = max(m, lst[i - k])
    s = max(s, lst[i] + m)

print(s)
