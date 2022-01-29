# 숫자 카드 게임

# N * M 행렬이 입력으로 들어올 때 각 행에서 가장 작은 수들 중 가장 큰 수를 출력하는 프로그램을 작성하시오

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
min_list = []
for i in range(n):
    min_list.append(min(arr[i]))
print(max(min_list))
