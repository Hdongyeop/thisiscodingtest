# https://www.acmicpc.net/problem/12015
import bisect

n = int(input())
li = list(map(int, input().split()))
sequence = [li[0]]
for i in range(1, len(li)):
    if li[i] > sequence[-1]:
        sequence.append(li[i])
    else:
        sequence[bisect.bisect_left(sequence, li[i])] = li[i]
print(len(sequence))
# print(' '.join(map(str, sequence)))