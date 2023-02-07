# 선긋기 (https://www.acmicpc.net/problem/2170)

import sys

n = int(input())
input = sys.stdin.readline
input_list = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
input_list.sort()

total_len = 0
for i in range(n):
    if i == 0:
        start, end = input_list[i]
        total_len = end - start
    else:
        if input_list[i][0] > start:
            if input_list[i][0] < end < input_list[i][1]:
                total_len += input_list[i][1] - end
                end = input_list[i][1]
            elif input_list[i][0] >= end:
                total_len += input_list[i][1] - input_list[i][0]
                start, end = input_list[i]
        else:
            if input_list[i][1] > end:
                total_len += input_list[i][1] - end
                end = input_list[i][1]

print(total_len)
