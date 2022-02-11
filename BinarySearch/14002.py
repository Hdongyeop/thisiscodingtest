# https://www.acmicpc.net/problem/14002

n = int(input())
li = list(map(int, input().split()))
dp = [1] * len(li)
for j in range(len(li)):
    for i in range(j):
        if li[j] > li[i]:
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))

cnt = max(dp)
res = []
for i in range(len(li)-1, -1, -1):
    if cnt == dp[i]:
        res.append(li[i])
        cnt -= 1
res = res[::-1]
print(' '.join(map(str, res)))
