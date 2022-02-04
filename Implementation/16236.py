# https://www.acmicpc.net/problem/16236

import sys, collections
_y, _x = 0, 0
cur_size = 2
eat_cnt = 0
fish_cnt = 0
time = 0
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if 0 < matrix[i][j] <= 6:
            fish_cnt += 1
        elif matrix[i][j] == 9:
            _y, _x = i, j

# 아기상어 위치도 0으로
matrix[_y][_x] = 0


def bfs(py, px):
    dq = collections.deque([(_y, _x, 0)])
    dist_list = []
    visited = [[False] * n for _ in range(n)]
    visited[py][px] = True
    min_dist = 2e9

    while dq:
        y, x, dist = dq.popleft()
        for _dir in dirs:
            dy = y + _dir[0]
            dx = x + _dir[1]
            if 0 <= dy < n and 0 <= dx < n and not visited[dy][dx]:
                if matrix[dy][dx] <= cur_size:
                    # 일단 방문 표시
                    visited[dy][dx] = True
                    # 자신보다 작은 고기가 있을 경우
                    if 0 < matrix[dy][dx] < cur_size:
                        min_dist = dist
                        dist_list.append((dist+1, dy, dx))
                    # 최소거리보다 작은 곳으로만 뻗어나감
                    if dist + 1 <= min_dist:
                        dq.append((dy, dx, dist+1))
    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False


while fish_cnt:
    res = bfs(_y, _x)
    if not res:
        break
    _y, _x = res[1], res[2]
    time += res[0]
    eat_cnt += 1
    fish_cnt -= 1
    if cur_size == eat_cnt:
        cur_size += 1
        eat_cnt = 0
    matrix[_y][_x] = 0

print(time)
