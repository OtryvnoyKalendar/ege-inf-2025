f = open('273_B.txt')
n = int(f.readline())
data = []

for i in range(n):
    km, prob = map(int, f.readline(). split())
    data.append([km, (prob + 35) // 36])

k_do = n * [0]
k_do[0] = data[0][1]
for i in range(1, n):
    k_do[i] = k_do[i - 1] + data[i][1]

s0 = 0
for i in range(n):
    s0 = s0 + abs(data[i][0] - data[0][0]) * data[i][1]

prices = [s0]
for i in range(1, n):
    s0 = s0 + (data[i][0] - data[i-1][0]) * k_do[i-1] \
    - (data[i][0] - data[i-1][0]) * (k_do[-1] - k_do[i-1])
    prices.append(s0)

print(min(prices))
