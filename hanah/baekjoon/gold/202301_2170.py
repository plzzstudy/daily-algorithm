# 선긋기 (https://www.acmicpc.net/problem/2170)

import sys

input = sys.stdin.readline
n = int(input())
input_list = sorted([tuple(map(int, input().rstrip().split())) for _ in range(n)], key=lambda x: x[0])

start, end = input_list[0]
total_len = end - start
for x, y in input_list[1:]:
    if end <= x:
        total_len += y - x
        start, end = x, y
    elif end < y:
        total_len += y - end
        end = y

print(total_len)
