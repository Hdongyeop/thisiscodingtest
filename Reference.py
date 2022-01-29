# 소수점 계산을 할 때 정확히 계산되지 않는다.
a = 0.3 + 0.6
print(a)  # 0.899999999

if a == 0.9:
    print(True)
else:
    print(False)  # result

# round 함수를 통해 어디까지 반올림 할 것인지 정할 수 있다.
a = 0.3 + 0.6
print(round(a, 4))  # 0.9 (소수점 5번째자리에서 반올림)

if round(a, 4) == 0.9:
    print(True)  # result
else:
    print(False)

# 크기가 N이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# List comprehension 을 이용한 2차원 배열(N*M) 만들기
n, m = 3, 4
arr = [[0] * m for _ in range(n)]
print(arr)

n, m, l = 3, 4, 5
arr = [[[0] * m for _ in range(n)] for _ in range(l)]
print(len(arr[0]))

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)

# Dictionary(사전형식)
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

# Set(집합 형식)
data = {1, 1, 2, 2, 3, 4, 4, 5}
print(data)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a | b)
print(a & b)
print(a - b)

# Input data
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

n, m, k = map(int, input().split())
print(n, m, k)

# Sort
data = [('김길동', 35), ('이순신', 50), ('아무개', 50)]
res = sorted(data, key=lambda x: x[0])  # Secondary key
print(res)
res = sorted(res, key=lambda x: x[1], reverse=True)  # Prime Key
print(res)

# itertools
data = ['A', 'B', 'C']

from itertools import permutations, combinations
# 순열
permute_result = list(permutations(data, 3))
print(permute_result)
# 조합
combine_result = list(combinations(data, 2))
print(combine_result)

from itertools import product, combinations_with_replacement
# 중복 순열
product_result = list(product(data, repeat=2))
print(product_result)
# 중복 조합
combine_replacement_result = list(combinations_with_replacement(data, 2))
print(combine_replacement_result)

import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


data = [1, 3, 5, 6, 7, 2, 4, 9, 8, 0]
# 기본적으로는 최소힙(min heap)이기 때문에 오름차순으로 정렬된다.
res = heapsort(data)
print(res)

# bisect
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# collections
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))

from collections import Counter
data = ['red', 'red', 'blue', 'blue', 'blue', 'green']
counter = Counter(data)
print(counter)
print(dict(counter))
print(counter['blue'])
