# https://www.acmicpc.net/problem/1439

data = [0] * 2
_list = list(map(int, list(input())))
data[_list[0]] += 1
for i in range(1, len(_list)):
    if _list[i] != _list[i-1]:
        data[_list[i]] += 1
print(min(data))
