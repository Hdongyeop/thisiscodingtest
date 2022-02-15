# https://www.acmicpc.net/problem/3020
import bisect
from sys import stdin

n, h = map(int, stdin.readline().rstrip().split())
up, down = [], []
for i in range(n):
    x = int(stdin.readline().rstrip())
    if i % 2 == 0:
        down.append(x)
    else:
        up.append(x)

up.sort()
down.sort()

_min = n+1
cnt = 1

for height in range(1, h+1):
    up_idx, down_idx = bisect.bisect_left(up, (h+1)-height), bisect.bisect_left(down, height)
    obstacles = n - (up_idx + down_idx)
    if obstacles < _min:
        _min = obstacles
        cnt = 1
    elif obstacles == _min:
        cnt += 1

print(_min, cnt)
