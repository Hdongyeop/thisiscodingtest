# 바닥 공사

n = int(input())
dp = [0] * 1001
dp[0], dp[1], dp[2], dp[3] = 0, 1, 3, 5
for i in range(4, n):
    _sum = 0
    for x in range(1, i//2 + 1):
        _sum += (dp[x] * dp[i-x])
    dp[i] = _sum % 796796
print(dp[n])
