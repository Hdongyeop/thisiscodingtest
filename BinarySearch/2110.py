# https://www.acmicpc.net/problem/2110
import sys
sys.setrecursionlimit(10**7)

n, c = map(int, sys.stdin.readline().rstrip().split())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))
li.sort()


def binary_search(arr, s, e):
    while s <= e:
        mid = (s + e) // 2
        cur = arr[0]
        cnt = 1
        for i in range(1, len(arr)):
            if arr[i] - cur >= mid:
                cnt += 1
                cur = arr[i]

        if cnt >= c:
            global res
            res = mid
            s = mid + 1
        elif cnt < c:
            e = mid - 1


start = 1
end = li[-1] - li[0]
binary_search(li, start, end)
print(res)
