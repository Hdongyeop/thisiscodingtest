# https://www.acmicpc.net/problem/3190

import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = []
for _ in range(k):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp[0] -= 1
    tmp[1] -= 1
    apple.append(tmp)
l = int(sys.stdin.readline())
change = ['N'] * 10001
for _ in range(l):
    tmp = sys.stdin.readline().split()
    change[int(tmp[0])] = tmp[1]

snake = deque([[0, 0]])
_time = 0
_y, _x = 0, 0
_dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동 남 서 북
cur_dir = 0

while True:
    # check apple
    if [_y, _x] in apple or _time == 0:
        if _time != 0:
            apple.remove([_y, _x])
    else:
        snake.pop()

    # move
    _y += _dir[cur_dir][0]
    _x += _dir[cur_dir][1]
    _time += 1

    if _y < 0 or _y >= n or _x < 0 or _x >= n or [_y, _x] in snake:
        print(_time)
        break

    snake.appendleft([_y, _x])

    # check change dir
    if change[_time] == 'D':
        cur_dir += 1
        cur_dir %= 4
    elif change[_time] == 'L':
        cur_dir += 3
        cur_dir %= 4

