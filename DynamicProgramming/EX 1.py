# 1로 만들기

# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같다
# (1) X가 5로 나누어 떨어지면 5로 나눈다
# (2) X가 3으로 나누어 떨어지면 3으로 나눈다
# (3) X가 2로 나누어 떨어지면 2로 나눈다
# (4) X에서 1을 뺀다
# 이러한 연산 4개를 이용해 X를 1로 만들려고 할 때 연산을 사용하는 횟수의 최소값을 출력하시오

# 26
# ANS = 3

n = int(input())
arr = [int(1e9)] * 30001
arr[n] = 0


# Top-down
def dp(x):
    if x == 1:
        return
    if x % 5 == 0:
        arr[x//5] = min(arr[x//5], arr[x] + 1)
        dp(x//5)
    if x % 3 == 0:
        arr[x//3] = min(arr[x//3], arr[x] + 1)
        dp(x//3)
    if x % 2 == 0:
        arr[x//2] = min(arr[x//2], arr[x] + 1)
        dp(x//2)
    arr[x-1] = min(arr[x-1], arr[x] + 1)
    dp(x-1)


dp(n)
print(arr[1])


# Bottom-Up
for i in range(2, n+1):
    arr[i] = arr[i-1] + 1
    if i % 5 == 0:
        arr[i] = min(arr[i], arr[i//5] + 1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)

print(arr[n])