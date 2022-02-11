# 부품 찾기
# 부품마다 정수형태의 고유한 번호가 존재할 때 손님이 찾는 부품이 있는지 살펴본다
# 가게에는 N개의 부품이 있고 손님은 M개의 부품을 찾는다

# 5
# 8 3 7 9 2
# 3
# 5 7 9
# ANS = no yes yes

import sys


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return None


n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

m = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
for stuff in arr2:
    if binary_search(arr, stuff, 0, n-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')

# 어떤 수의 존재만 확인하면 되기 때문에 계수정렬, Set 자료형을 통해서도 풀 수 있다.
