# 효율적인 화폐 구성

n, m = map(int, input().split())
li = [10001] * 10001
money = []
for _ in range(n):
    idx = int(input())
    money.append(idx)
    li[idx] = 1
for i in range(1, m+1):
    _min = li[i]
    for x in money:
        if i-x > 0:
            _min = min(_min, li[i-x] + 1)
    li[i] = _min
if li[m] == 10001:
    print(-1)
else:
    print(li[m])

