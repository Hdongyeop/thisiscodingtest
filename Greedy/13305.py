# https://www.acmicpc.net/problem/13305

n = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = []
now_cost = cost[0]
passed_len = 0

for i in range(n-1):
    passed_len += length[i]
    if cost[i+1] < now_cost:
        res.append([now_cost, passed_len])
        now_cost = cost[i+1]
        passed_len = 0

if passed_len != 0:
    res.append([now_cost, passed_len])

_sum = sum(data[0] * data[1] for data in res)
print(_sum)

