# https://www.acmicpc.net/problem/1072

import sys

x, y = map(int, input().split())
old = int(100 * y/x)

if old >= 99:
    print(-1)
    sys.exit(0)

start = 0
end = x
while start <= end:
    mid = (start + end) // 2
    cur = int(100 * (y+mid)/(x+mid))
    if old < cur:
        end = mid - 1
    else:
        start = mid + 1

print(start)
