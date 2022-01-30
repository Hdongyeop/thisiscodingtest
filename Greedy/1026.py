# https://www.acmicpc.net/problem/1026

n = int(input())
list_a = sorted(list(map(int, input().split())))
list_b = sorted(list(map(int, input().split())), reverse=True)

print(sum(list(list_a[i] * list_b[i] for i in range(n))))
