# https://www.acmicpc.net/problem/2512
import sys

n = int(input())
li = list(map(int, input().split()))
money = int(input())
if money > sum(li):
    print(max(li))
    sys.exit(0)
start = 0
end = max(li)
res = []
while start <= end:
    mid = (start + end) // 2
    tmp = list(map(lambda x: mid if x > mid else x, li))
    if sum(tmp) <= money:
        start = mid + 1
        if sum(res) < sum(tmp):
            res = tmp
    else:
        end = mid - 1

print(max(res))