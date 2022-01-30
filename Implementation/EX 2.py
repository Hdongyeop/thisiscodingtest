# 왕실의 나이트

# 8 * 8 좌표 평면
#    a  b  c  d  e  f  g  h
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# 이 좌표평면에서 나이트는 수직으로 두 칸 이동 후 수평으로 한 칸 이동 혹은
# 수평으로 두 칸 이동 후 수직으로 한 칸 이동을 할 수 있다.
# 이 때 나이트의 위치가 "a1"의 형식으로 주어질 때 나이트가 이동 할 수 있는 위치의 개수는 몇 개 인가?

pos = list(input())
pos[0], pos[1] = int(pos[1]), ord(pos[0]) - 96
print(pos)

moves = [[-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1]]
cnt = 0

for move in moves:
    tmp_y = pos[0] + move[0]
    tmp_x = pos[1] + move[1]
    if 0 < tmp_y < 9 and 0 < tmp_x < 9:
        cnt += 1

print(cnt)
