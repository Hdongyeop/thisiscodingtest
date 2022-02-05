# 음료수 얼려 먹기

# N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시 될 때
# 총 아이스크림의 개수는 몇 개 인가

# 4 5
# 00110
# 00011
# 11111
# 00000
# output = 3

import collections

n, m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]
stack = collections.deque([])
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(y, x):
    if mat[y][x] == 1:
        return False

    stack.append((y, x))

    while stack:
        _y, _x = stack.pop()
        mat[_y][_x] = 1
        for _dir in dirs:
            dy = _y + _dir[0]
            dx = _x + _dir[1]
            if dx < 0 or dx >= m or dy < 0 or dy >= n or mat[dy][dx] == 1:
                continue
            stack.append((dy, dx))
        if len(stack) == 0:
            return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        stack = collections.deque([])
        if dfs(i, j):
            cnt += 1

print(cnt)
