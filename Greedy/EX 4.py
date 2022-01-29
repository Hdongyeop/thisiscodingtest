# 1이 될 때까지

# 숫자 n이 주어질 때 이 숫자에 대하여 두 가지 연산을 할 수 있다.
# 1. n -= 1
# 2. n //= k (n이 k의 배수일 경우에만)
# 두 연산을 반복하며 1을 만들 때 최소의 연산 횟수를 구하라.

# 1
n, k = map(int, input().split())
cnt = 0
while n != 1:
    cnt += 1
    if n % k == 0:
        n /= k
        continue
    n -= 1
print(cnt)

# 2
n, k = map(int, input().split())
cnt = 0
while True:
    # target을 n보다 작은 k의 배수로 만듬
    target = (n // k) * k
    # n이 target이 될 때까지 -1을 계속함
    cnt += (n - target)
    n = target
    # 더 이상 나누기를 못하게 됬을 때 stop
    if n < k:
        break
    cnt += 1
    n //= k

# 최종적으로 n은 1이 되어야 하므로 cnt에는 n-1을 더해준다
cnt += (n-1)
print(cnt)
