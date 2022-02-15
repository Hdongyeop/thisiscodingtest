# https://www.acmicpc.net/problem/10815
import bisect
from sys import stdin

n = int(input())
li1 = list(map(int, stdin.readline().rstrip().split()))
li1.sort()
m = int(input())
li2 = list(map(int, stdin.readline().rstrip().split()))
ans = []


def binary_search(li, x):
    start = 0
    end = len(li) - 1
    while start <= end:
        mid = (start + end) // 2
        if li[mid] > x:
            end = mid - 1
        elif li[mid] < x:
            start = mid + 1
        elif li[mid] == x:
            return 1
    return 0


for x in li2:
    ans.append(binary_search(li1, x))
print(' '.join(map(str, ans)))