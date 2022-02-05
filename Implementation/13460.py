# https://www.acmicpc.net/problem/13460

import collections

n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]
ry, rx, by, bx, oy, ox = 0, 0, 0, 0, 0, 0
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'R':
            ry = i
            rx = j
        elif mat[i][j] == 'B':
            by = i
            bx = j
        elif mat[i][j] == 'O':
            oy = i
            ox = j


def bfs():
    count = 0
    dq = collections.deque([(ry, rx, by, bx, count)])
    res = set()

    while dq:
        # 현재 R과 B의 위치
        _ry, _rx, _by, _bx, cnt = dq.popleft()

        if cnt >= 10:
            break
        cnt += 1

        # Move
        for _dir in dirs:
            dry, drx, dby, dbx = _ry, _rx, _by, _bx
            r_cnt, b_cnt = 0, 0
            r_check, b_check = False, False

            # 한 칸씩 방향 끝까지 움직임
            while mat[dby + _dir[0]][dbx + _dir[1]] != '#':
                dby += _dir[0]
                dbx += _dir[1]
                b_cnt += 1
                if dby == oy and dbx == ox:
                    b_check = True

            while mat[dry + _dir[0]][drx + _dir[1]] != '#':
                dry += _dir[0]
                drx += _dir[1]
                r_cnt += 1
                if dry == oy and drx == ox:
                    r_check = True

            # 공이 구멍에 들어 갔을 때
            if r_check and b_check:
                res.add(-1)
                continue
            if r_check:
                res.add(cnt)
                return res
            if b_check:
                res.add(-1)
                continue

            # 만약 겹치게 된다면 늦게온 공을 한 칸 뒤로 물림
            if dby == dry and dbx == drx:
                if r_cnt < b_cnt:
                    dby -= _dir[0]
                    dbx -= _dir[1]
                else:
                    dry -= _dir[0]
                    drx -= _dir[1]

            # 둘중에 하나라도 움직였으면 뻗어 나가기
            if dry != _ry or drx != _rx or dby != _by or dbx != _bx:
                dq.append((dry, drx, dby, dbx, cnt))

    return res


_list = sorted(list(bfs()))
# print(_list)
if len(_list) == 0:
    print(-1)
elif len(_list) == 1:
    print(_list[0])
else:
    print(_list[1])
