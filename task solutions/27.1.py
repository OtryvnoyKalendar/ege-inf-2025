# 1
file = open("tm24/27B_18677.txt")
# x = file.readline() # если есть X Y в начале файла
# print(x)
data = [tuple(map(float, x.replace(",", ".").split())) for x in file]

print(len(data))

# 2
from math import dist
# или своя функция

# 3
clusters = []
while data:
    cluster = [data.pop()]
    for p in cluster:
        soseds = [p1 for p1 in data if dist(p1, p) < 0.8]
        cluster += soseds
        for p1 in soseds:
            data.remove(p1)
    clusters.append(cluster)

res = [len(cluster) for cluster in clusters]
print(res, sum(res))

# 4
from turtle import *
from random import random
tracer(0)
up()
sc = 25
screensize(4000, 4000)
for cluster in clusters:
    color = random(), random(), random()
    for x,y in cluster:
        goto(x*sc, y*sc)
        dot(5, color)
exitonclick()

# иногда нужна проверка на аномалии
clusters = [x for x in clusters if len(x) >= 30]

# 5
def get_center(cluster):
    res = []
    for p in cluster:
        dist_sum = sum([dist(p1, p) for p1 in cluster])
        res.append((dist_sum, p))
    return min(res)[1]

# 6
n = len(clusters)
centers = [get_center(cluster) for cluster in clusters]
px = sum(x for x,y in centers)/n
py = sum(y for x,y in centers)/n
print(int(abs(px*100_000)), int(abs(py*100_000)))


