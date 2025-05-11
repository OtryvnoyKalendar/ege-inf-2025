f = open('271B.txt')
n = int(f.readline())
s_max = 0
d_min = 10**25

for i in range(n):
    a, b = map(int, f.readline().split())
    s_max += max(a, b)
    if abs(a - b) % 3 != 0:
        d_min = min(d_min, abs(a - b))

if s_max % 3 != 0:
    print(s_max)
else:
    print(s_max - d_min)
