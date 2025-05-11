from re import *

data = open("24-215.txt").readline()
pattern = r"(?:[123][ABC][123])+"

res = []
for i in range(len(data)):
    c = search(pattern, data)
    if c:
        res.append(len(c[0]))
        data = data[c.start():]
    data = data[1:]

print(max(res) / 3)

# 164.0
