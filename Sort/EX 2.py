# 성적이 낮은 순서로 학생 출력하기

# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 점수로 구분된다.
# 각 학생의 이름과 점수가 주어졌을 때 성적이 낮은 순서대로 이름을 출력하는 프로그램을 작성하시오.

# 2
# 홍길동 95
# 이순신 77
# ANS = 이순신 홍길동

n = int(input())
infos = []
for _ in range(n):
    info = input().split()
    infos.append((info[0], int(info[1])))
infos.sort(key=lambda x: x[1])
for info in infos:
    print(info[0], end=' ')
