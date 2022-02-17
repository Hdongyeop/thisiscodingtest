# 개미전사

# 식량창고의 개수 n이 주어지고 그 다음줄에는 각 창고마다 저장되어 있는 식량의 개수가 주어진다
# 인접한 식량창고를 공격할 경우에는 들키기 때문에 최소 한칸 이상이 띄워진 창고만을 공격할 수 있다
# 이 때 식량을 최대로 얻고자 할 때 그 값을 구하시오

# 4
# 1 3 1 5
# ANS = 8

n = int(input())
li = list(map(int, input().split()))
dp = [0] * len(li)
dp[0], dp[1] = li[0], max(li[0], li[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + li[i])
print(max(dp))
