# https://www.acmicpc.net/problem/2565

n = int(input())
li = []
values = []
dp = [0] * n
for _ in range(n):
    _from, _to = map(int, input().split())
    li.append((_from, _to))
li.sort()
for i in range(n):
    values.append(li[i][1])
for i in range(n):
    for j in range(i):
        if values[i] > values[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))

