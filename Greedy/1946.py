# https://www.acmicpc.net/problem/1946
import sys

for _ in range(int(sys.stdin.readline())):
    tc = int(sys.stdin.readline())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(tc)]
    points.sort()
    cur_point = points[0][1]
    cnt = 1
    for i in range(1, len(points)):
        if cur_point > points[i][1]:
            cur_point = points[i][1]
            cnt += 1
    print(cnt)
