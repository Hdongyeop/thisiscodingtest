# https://www.acmicpc.net/problem/2075
import heapq

n = int(input())
heap = []
for _ in range(n):
    _list = list(map(int, input().split()))
    for num in _list:
        heapq.heappush(heap, num)
        if len(heap) > n:
            heapq.heappop(heap)

print(heap[0])
