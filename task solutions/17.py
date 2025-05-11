f = open('17-1.txt')
lst = [int(x) for x in f]
ans = []

for i in range(1, len(lst) - 1):
    if lst[i] < lst[i - 1] and lst[i] < lst[i+1]:
        ans.append(lst[i])

print(len(ans), max(ans))
