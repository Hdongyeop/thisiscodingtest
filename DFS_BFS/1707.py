# https://www.acmicpc.net/problem/1707
import collections
import sys


def bfs(idx):
    dq = collections.deque()
    dq.append((idx, 1))  # index, color

    while dq:
        idx, color = dq.popleft()
        visited[idx] = color

        nodes = graph[idx]
        for node in nodes:
            if visited[node] == 0:
                if color == 1:
                    dq.append((node, 2))
                elif color == 2:
                    dq.append((node, 1))
            elif visited[node] == color:
                return False
    return True


k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    visited = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        f, t = map(int, sys.stdin.readline().split())
        graph[f].append(t)
        graph[t].append(f)

    res = True

    for i in range(1, v + 1):
        if visited[i] == 0:
            res &= bfs(i)

    if res:
        print('YES')
    else:
        print('NO')
