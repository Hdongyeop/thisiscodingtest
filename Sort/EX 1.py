# 위에서 아래로

# 하나의 수열에는 다양한 수가 존재한다. 이런 수들은 크기에 상관없이 나열되어 있다. 이 수들을 큰 수부터 작은 수로
# 나열해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 작성하시오.

# 3
# 15
# 27
# 12
# ANS = 27 15 12

n = int(input())
res = []
for _ in range(n):
    res.append(input())
res.sort(reverse=True)
print(' '.join(res))
