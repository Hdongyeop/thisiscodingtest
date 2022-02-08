# https://www.acmicpc.net/problem/2573
import collections
import copy

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def Ice_Check():
    tmp = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if mat[i][j] > 0:
                tmp.append((i, j))
    return tmp


def Decrease():
    tmp = copy.deepcopy(mat)
    for p in ice_list:
        i = p[0]
        j = p[1]
        for di in dirs:
            dy = i + di[0]
            dx = j + di[1]
            if 0 <= dy < n and 0 <= dx < m and mat[dy][dx] == 0 and tmp[i][j] > 0:
                tmp[i][j] -= 1
    return tmp


def Check():
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    global ice_list
    ice_list = Ice_Check()
    if len(ice_list) == 0:
        return 987654321
    for p in ice_list:
        i = p[0]
        j = p[1]
        if not visited[i][j]:
            cnt += 1
            dq = collections.deque()
            dq.append((i, j))
            visited[i][j] = True

            while dq:
                _y, _x = dq.popleft()

                for di in dirs:
                    dy = _y + di[0]
                    dx = _x + di[1]
                    if 0 <= dy < n and 0 <= dx < m and not visited[dy][dx] and mat[dy][dx] != 0:
                        dq.append((dy, dx))
                        visited[dy][dx] = True

    return cnt


res = 0
while True:
    c = Check()
    if c >= 2:
        if c == 987654321:
            print(0)
            break
        else:
            print(res)
            break
    res += 1
    mat = Decrease()
