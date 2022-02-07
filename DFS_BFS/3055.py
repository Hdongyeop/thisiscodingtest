# https://www.acmicpc.net/problem/3055
import collections
import sys

r, c = map(int, sys.stdin.readline().split())
mat = [list(input()) for _ in range(r)]
d, s = (), ()
w = []
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(r):
    for j in range(c):
        if mat[i][j] == 'D':
            d = (i, j)
        if mat[i][j] == '*':
            w.append((i, j))
        if mat[i][j] == 'S':
            s = (i, j)


def bfs():
    cnt = 0
    wdq = collections.deque()
    sdq = collections.deque()

    for i in range(len(w)):
        wdq.append((w[i][0], w[i][1]))
    sdq.append((s[0], s[1]))

    while sdq or wdq:
        # 물 확장
        for _ in range(len(wdq)):
            wy, wx = wdq.popleft()
            for di in dirs:
                dwy = wy + di[0]
                dwx = wx + di[1]
                if 0 <= dwy < r and 0 <= dwx < c and (mat[dwy][dwx] == '.' or mat[dwy][dwx] == 'S') and mat[dwy][dwx] != '*':
                    mat[dwy][dwx] = '*'
                    wdq.append((dwy, dwx))

        # 고슴도치 확장
        for _ in range(len(sdq)):
            sy, sx = sdq.popleft()

            # 비버 집 체크
            if sy == d[0] and sx == d[1]:
                return cnt

            for di in dirs:
                dsy = sy + di[0]
                dsx = sx + di[1]
                if 0 <= dsy < r and 0 <= dsx < c and (mat[dsy][dsx] == '.' or mat[dsy][dsx] == 'D') and mat[dsy][dsx] != 'S':
                    mat[dsy][dsx] = 'S'
                    sdq.append((dsy, dsx))

        cnt += 1

    return 'KAKTUS'


print(bfs())
