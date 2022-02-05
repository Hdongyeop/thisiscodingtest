# 미로 탈출

# N * M 크기의 직사각형에서 (0,0)에서 출발하여 (n, m)으로 도달할 때 걸리는 시간을 구하라
# 벽은 0 이고 길은 1으로 표시된다.

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# ANS : 10

from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]
dq = deque([(0, 0)])
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs():
    while dq:
        y, x = dq.popleft()
        for _dir in dirs:
            dy = y + _dir[0]
            dx = x + _dir[1]
            if 0 <= dy < n and 0 <= dx < m and mat[dy][dx] == 1:
                dq.append((dy, dx))
                mat[dy][dx] = mat[y][x] + 1
                if dy == n-1 and dx == m-1:
                    print(mat[dy][dx])
                    return


bfs()
