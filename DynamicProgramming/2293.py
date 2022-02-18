# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
li = []
dp = [0] * (k+1)
for _ in range(n):
    li.append(int(input()))
li.sort()
for i in range(n):
    if li[i] <= k:
        dp[li[i]] += 1
        for j in range(li[i]+1, k+1):
            dp[j] += dp[j-li[i]]
print(dp[k])

