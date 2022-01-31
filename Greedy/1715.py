# https://www.acmicpc.net/problem/1715
import heapq

n = int(input())
pq = []
for _ in range(n):
    heapq.heappush(pq, int(input()))
res = 0
while True:
    if len(pq) == 1:
        break
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    res += a+b
    heapq.heappush(pq, a+b)

# res += heapq.heappop(pq)
print(res)
