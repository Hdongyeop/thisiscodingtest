# Binary Search(이진 검색)
1. 리스트 내에서 빠르게 검색하는 방법
2. 정렬되어 있어야 함
3. 범위를 반씩 줄어간다는 아이디어
4. 재귀 또는 반복문으로 구현

***
## 구현
+ 재귀
```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# Input Processing
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

res = binary_search(arr, target, 0, n-1)
if res == None:
    print("There is no element")
else:
    print(res + 1)
```
+ 반복문
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return None

# Input Processing
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

res = binary_search(arr, target, 0, n-1)
if res == None:
    print("There is no element")
else:
    print(res + 1)
```