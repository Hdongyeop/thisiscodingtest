# https://www.acmicpc.net/problem/14499

n, m, y, x, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
actions = list(map(int, input().split()))
_dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # 동 서 북 남
dice = [0] * 6
lower_side = 5  # 밑 면
upper_side = 0  # 윗 면

for action in actions:
    # 벽 처리
    dy = y + _dir[action - 1][0]
    dx = x + _dir[action - 1][1]
    if dy < 0 or dy >= n or dx < 0 or dx >= m:
        continue
    else:
        y = dy
        x = dx

    # 주사위 뒤집기
    if action == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif action == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif action == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif action == 4:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

    # mat의 값이 0이면 주사위 밑면에 있는 값 복사
    if mat[y][x] == 0:
        mat[y][x] = dice[lower_side]
    else:
        dice[lower_side] = mat[y][x]
        mat[y][x] = 0

    print(dice[upper_side])
