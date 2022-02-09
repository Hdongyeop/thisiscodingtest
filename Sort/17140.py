# https://www.acmicpc.net/problem/17140
import collections

r, c, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(3)]
cnt = 0


def Mat_sort(matrix):
    max_len = 0
    for i in range(len(matrix)):
        counter = dict(collections.Counter(matrix[i]))
        kv = list(zip(counter.keys(), counter.values()))
        kv.sort(key=lambda x: (x[1], x[0]))
        tmp = []
        for data in kv:
            k, v = data
            if k == 0:
                pass
            else:
                tmp.append(k)
                tmp.append(v)
        if len(tmp) > max_len:
            max_len = len(tmp)
        matrix[i] = tmp

    # 0 추가
    for row in matrix:
        while len(row) < max_len:
            row.append(0)


# 가운데를 기준으로 뒤집기
def Reverse_RL(matrix):
    row_len = len(matrix[0])
    mid = row_len // 2
    for row in range(len(matrix)):
        for i in range(mid):
            matrix[row][i], matrix[row][row_len-i-1] = matrix[row][row_len-i-1], matrix[row][i]


while True:
    if cnt > 100:
        cnt = -1
        break
    if r-1 < len(mat) and c-1 < len(mat[0]) and mat[r-1][c-1] == k:
        break
    if len(mat) >= len(mat[0]):  # row >= column
        Mat_sort(mat)
    else:
        # 시계방향 90도 회전
        mat = [k[::-1] for k in zip(*mat)]
        Mat_sort(mat)
        mat = [list(k[::-1]) for k in zip(*mat)]
        Reverse_RL(mat)
    cnt += 1

print(cnt)
