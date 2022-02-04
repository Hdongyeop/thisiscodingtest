# https://www.acmicpc.net/problem/5430
import collections
import sys, re

t = int(sys.stdin.readline())
for _ in range(t):
    ops = list(input())

    n = int(sys.stdin.readline())
    arr_str = sys.stdin.readline()
    arr = re.findall('[\d]+', arr_str)
    arr = collections.deque(arr)

    reverse_flag = False
    empty_flag = False

    for op in ops:
        if op == 'R':
            reverse_flag = not reverse_flag
        elif op == 'D':
            if len(arr) != 0:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                empty_flag = True
                break

    if reverse_flag:
        arr.reverse()

    if not empty_flag:
        print('['+','.join(arr)+']')

