f = open('26-3.txt')
k = int(f.readline())
n = int(f.readline())
time = []

for i in range(n):
    a = [int(x) for x in f.readline().split()]
    time.append(a)

time.sort()
fin = [0] * k
c = 0
c1 = 0

for i in range(len(time)):
    for j in range(len(fin)):
        if time[i][0] > fin[j]:
            fin[j] = time[i][1]
            c += 1
            c1 = j + 1
            break

print(c, c1)
