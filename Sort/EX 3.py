# 두 배열의 원소 교체

# N의 크기를 가지는 A, B 두 배열이 존재한다. 이 배열에는 모두 자연수가 들어가 있다.
# 두 배열의 값을 교환할 수 있는 횟수가 K번 주어진다고 할 때 A의 배열의 총 합을 최대로 만드는
# 프로그램을 작성하라.

# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
# ANS = 26

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
for i in range(k):
    if b[i] > a[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
