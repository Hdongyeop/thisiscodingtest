# https://www.acmicpc.net/problem/1789

s = int(input())
_sum = 0
i = 1
while True:
    _sum += i
    if _sum > s:
        i -= 1
        break
    i += 1
print(i)