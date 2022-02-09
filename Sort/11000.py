# https://www.acmicpc.net/problem/11000
import sys
import heapq

n = int(sys.stdin.readline().rstrip())
_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
_list.sort(key=lambda x: x[0])

heap = []
heapq.heappush(heap, _list[0][1])

for i in range(1, n):
    if heap[0] <= _list[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, _list[i][1])

print(len(heap))
