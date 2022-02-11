# https://www.acmicpc.net/problem/2887
import sys


def Find(parent, x) -> int:
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]


def Union(parent, a, b):
    parent_a = Find(parent, a)
    parent_b = Find(parent, b)
    # 작은 노트가 루트가 되게 합치기
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


def Check_Cycle(parent, edge) -> bool:
    c, a, b = edge
    if Find(parent, a) == Find(parent, b):
        return True
    else:
        Union(parent, a, b)
    return False


n = int(sys.stdin.readline().rstrip())
points = []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    points.append([x, y, z, i])
# Parent
p = [x for x in range(n)]

edges = []
for k in range(3):
    points.sort(key=lambda x: x[k])
    prev_node = points[0][3]
    for i in range(1, n):
        cur_node = points[i][3]
        edges.append((abs(points[i][k] - points[i-1][k]), prev_node, cur_node))
        prev_node = cur_node
edges.sort()

res = []
for edge in edges:
    if Check_Cycle(p, edge):
        pass
    else:
        res.append(edge[0])

print(sum(res))
