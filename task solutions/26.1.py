f = open('26-1.txt')
s, n = map(int, f.readline().split())
a = sorted([int(x) for x in f])

s1 = 0
c = 0
b = 0

for i in range(n):
    if s1 + a[i] <= s:
        s1 += a[i]
        c += 1
        b = a[i]
        a[i] = 0

print(c, 'макс число')
s1 = s1 - b
a = a[::-1]

for i in range(n):
    if a[i] != 0 and s1 + a[i] <= s:
        print(a[i], 'макс файл')
        break
