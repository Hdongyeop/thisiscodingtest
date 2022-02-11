# 떡볶이 떡 만들기

# 19, 14, 10, 17cm의 떡이 있을 때 15cm의 높이로 자르면 각 떡은
# 4, 0, 0, 2cm 만큼의 떡이 떨어져 나오게 된다. 따라서 손님이 가져가는 떡의 길이는 6cm이다
# 이런 조건에서 손님이 요청한 떡의 길이 이상을 만족하는 최대의 높이는 몇인가

n, m = map(int, input().split())
li = list(map(int, input().split()))

start = 0
end = max(li)
res = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in li:
        if x > mid:
            total += (x - mid)
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
