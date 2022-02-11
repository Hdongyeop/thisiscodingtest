# https://www.acmicpc.net/problem/2467

n = int(input())
_list = list(map(int, input().split()))
_list.sort()

s, e = 0, n-1
res = ()
min_value = 2e9
while s < e:
    _sum = _list[s] + _list[e]
    if abs(_sum) <= min_value:
        min_value = abs(_sum)
        res = (_list[s], _list[e])

    if _sum == 0:
        res = (_list[s], _list[e])
        break
    elif _sum > 0:
        e -= 1
    elif _sum < 0:
        s += 1


print(' '.join(map(str, sorted(res))))

