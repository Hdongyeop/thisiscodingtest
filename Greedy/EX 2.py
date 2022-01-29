# 큰 수의 법칙

# N의 크기를 가지는 배열이 주어질 때 그 안의 숫자들을 M번 더해서
# 최대를 만드는 숫자를 구하라 단, 연속되는 인덱스는 K 번까지 가능하다
# (중복되는 숫자라도 인덱스가 다르면 다른것으로 본다)

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# 1
count = 0
res = 0
for i in range(M):
    if count == K:
        res += arr[-2]
        count = 0
        continue
    res += arr[-1]
    count += 1
print(res)

# 2
max_num_cnt = (M // (K+1)) * K + (M % (K+1))
second_num_cnt = M - max_num_cnt
res = arr[-1] * max_num_cnt + arr[-2] * second_num_cnt
print(res)
