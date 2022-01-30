# 게임 개발

# N * M 행렬을 입력받고 캐릭터의 위치를 입력받는다. 또한 캐릭터가 바라보고 있는 방향도 입력받는다.
# 방향은 0: 북, 1: 동, 2: 남, 3: 서 순서이다.
# 행렬의 입력값은 0일 경우 육지, 1일 경우 바다이다.
# 캐릭터는 바라보고 있는 방향을 기준으로 움직이며, 바다여서 이동이 불가능할 때는 시계 반대방향으로 90도 회전해서 움직인다.
# 모든 방향이 방문했거나 바다여서 이동이 불가능 할 경우에는 원래 바라보고 있는 방향을 기준으로 뒤로 한 칸 이동한다.
# 뒤로 이동하지 못할 경우 이동을 마무리한다. 출력으로는 방문한 지역의 개수를 나타낸다.

n, m = map(int, input().split())
y, x, _dir = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# print(mat)

visited[y][x] = 1
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북, 동, 남, 서
cnt = 1

while True:
    old_y = y
    old_x = x

    for i in range(4):
        dy = y + directions[_dir - i][0]
        dx = x + directions[_dir - i][1]
        if dy < 0 or dy >= n or dx < 0 or dx >= m or visited[dy][dx] == 1 or mat[dy][dx] == 1:
            continue
        y = dy
        x = dx
        visited[y][x] = 1
        _dir = directions.index(directions[_dir - i])
        cnt += 1
        break

    if old_y == y and old_x == x:
        # 모두 가본 칸이거나 바다이면 바라보는 방향 유지하고 한칸 뒤로
        dy = y + directions[_dir - 2][0]
        dx = x + directions[_dir - 2][1]
        # 이때 뒤쪽 칸이 바다거나 더 이상 갈 수 없는 경우에는 멈춘다.
        if dy < 0 or dy >= n or dx < 0 or dx >= m or mat[dy][dx] == 1:
            break
        y = dy
        x = dx

print(cnt)

