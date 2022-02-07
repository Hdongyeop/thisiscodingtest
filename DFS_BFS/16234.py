# https://www.acmicpc.net/problem/16234
import collections
import sys

n, L, R = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
day = 0


def bfs():
    union = [[-1] * n for _ in range(n)]
    union_sum = [0] * (n * n + 1)
    union_list = [list() for _ in range(n*n + 1)]
    cnt = 0

    # union 색칠 하기
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                dq = collections.deque()
                dq.append((i, j))

                while dq:
                    y, x = dq.popleft()
                    if union[y][x] == -1:
                        union[y][x] = cnt
                        union_sum[cnt] += mat[y][x]
                        union_list[cnt].append((y, x))
                        for di in dirs:
                            dy = y + di[0]
                            dx = x + di[1]
                            if 0 <= dy < n and 0 <= dx < n and L <= abs(mat[dy][dx] - mat[y][x]) <= R:
                                dq.append((dy, dx))
                cnt += 1

    # 평균값 나눠 주기
    for i in range(cnt):
        avg = union_sum[i] // len(union_list[i])  # 평균 값
        for p in union_list[i]:
            mat[p[0]][p[1]] = avg

    if cnt == n * n:
        return True
    else:
        return False


while not bfs():
    day += 1

print(day)
