# 상하좌우

# N * N 행렬이 존재할 때 맨 왼쪽 위를 시작점 (1,1)이라 하고 맨 오른쪽 아래를 (N, N)이라고 할 때
# (1,1)에서 출발하여 (L,R,U,D)의 문자열이 주어지면 어디로 도착하는지 나타내자

n = int(input())
plans = list(input().split())
directions = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cur = [1, 1]

for plan in plans:
    for i in range(len(directions)):
        if plan == directions[i]:
            if 0 < cur[0] + dy[i] < n and 0 < cur[1] + dx[i] < n:
                cur[0] += dy[i]
                cur[1] += dx[i]

print(cur[0], cur[1])

# 시각

# 정수 N 이 입력되면 0시 0분 0초 부터 N시 59분 59초까지의 모든 시각 속에 3이 하나라도 들어간 시간의 개수를 모두 구하라

n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            _str = str(i) + str(j) + str(k)
            if '3' in _str:
                cnt += 1
print(cnt)
