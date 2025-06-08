with open("27.1b.txt") as file:
    dots = [tuple(map(float, x.replace(",", ".").split())) for x in file]

print(len(dots))

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def get_cluster(p0):
    cluster = [p for p in dots if dist(p0, p) < 0.5]
    if len(cluster) > 0:
        for p in cluster:
            dots.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])

    return cluster

clusters = []
while len(dots) > 0:
    p0 = dots.pop()
    cluster = [p0] + get_cluster(p0)
    print("len =", len(cluster))
    clusters.append(cluster)

def center(cluster):
    m = []
    for p in cluster:
        dist_sum = sum(dist(p, p1) for p1 in cluster)
        m.append([dist_sum, p])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]
print([dot for dot in centers])
n = len(clusters)
px = sum(dot[0] for dot in centers)
py = sum(dot[1] for dot in centers)
print(int(px/n*10_000), int(py/n*10_000))

"""
A
100
len = 50
len = 50
[[5.51307169163416, 3.4700254913283], [0.898104452045083, 8.14956810985959]]
32055 58097
"""

"""
B
9999
len = 3333
len = 3333
len = 3333
[(1.35010146710459, 0.441722700965479),
(6.31722662214146, 3.20304212607331),
(1.89859074279227, 4.10549409017268)]
31886 25834
"""
