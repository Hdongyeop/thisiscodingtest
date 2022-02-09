# Sort
정렬(Sorting)은 ***데이터를 특정한 기준으로 순서대로 나열***하는 것을 뜻한다.
정렬 알고리즘은 많은 코딩테스트 유형에서 같이 활용되므로 필수적인 알고리즘이다.
또한 정렬된 데이터만이 이진탐색을 시행할 수 있으므로 선행작업으로써의 의미도 갖는다.

## 선택 정렬
아이디어 : 전체 데이터들 중 가장 작은 값을 선택해 가장 맨 앞에 놓는다.
그리고 그 다음 장 부터 시작하여 가장 작은 값을 선택해 맨 앞에 놓는다. 이를 반복한다.

```python
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[min_index], arr[i] = arr[i], arr[min_index]
```

## 삽입 정렬
아이디어 : 데이터를 하나씩 확인하면서 각 데이터를 적절한 위치에 삽입하자.
첫 번째 데이터를 어떤 가상에 배열에 넣는다고 생각하고 두 번째 데이터 부터는 
그 배열에서 적절한 위치에 삽입한다.

```python
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
```

## 퀵 정렬
아이디어 : 피벗(pivot)을 정하고 양쪽 끝에 포인터를 두고 계속 좁혀오면서 왼쪽포인터는 피벗보다 큰 것,
오른쪽 포인터는 피벗보다 작은 것을 가리키게 한다. 두 포인터 모두 가리켰으면 교환 한다.
그러다가 두 포인터가 교차하게 되면 그 때는 둘 중 작은 값을 가리키는 포인터와 피벗과 교환을 한다
이렇게 되면 배열은 [피벗보다 작음][피벗][피벗보다 큼] 이런 형식으로 놓여지게 된다.
여기서 왼쪽 배열과 오른쪽배열에 대해서 위와 같은 과정을 계속 반복하면 정렬이 되게 된다.

```python
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 종료조건(원소가 1개일 때)
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # pivot보다 더 큰 값 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 더 작은 값 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 교차했을 때
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 교차 안했으면 교환
        else:
            array[left], array[right] = array[right], array[left]
    
    # 양쪽 배열에 대해서 각자 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)
```

단순히 파이썬으로 [피벗보다 작음][피벗][피벗보다 큼]을 만들어 본다면 
리스트 내포를 통해 좀 더 쉽게 가능하다. 하지만 위에 보다는 조금 비효율적이다.
```python
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) == 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))
```

이외에도 **_계수정렬, 병합정렬_** 등이 존재한다.

***

## 코딩테스트에서의 정렬
1. 정렬 라이브러리로 풀 수 있는 문제
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제
3. 더 빠른 정렬이 필요한 문제(nlogn보다)

+ 우선순위 큐와도 관련이 많은것 같다.