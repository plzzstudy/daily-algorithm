'''
# 격자판 최대합

N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

▣ 출력설명 
최대합을 출력합니다.

▣ 입력예제 1
5
10 13 10 12 15 
12 39 30 23 11 
11 25 50 53 15 
19 27 29 37 27 
19 13 30 13 19

▣ 출력예제 1 
155

'''



# solution1
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

row_sum = [sum(arr[i]) for i in range(n)]
column_sum = [0] * n
cross_sum = [0] * 2

for i in range(n):
    for j in range(n):
        column_sum[i] += arr[j][i]

for i in range(n):
    cross_sum[0] += arr[i][i]
    cross_sum[1] += arr[i][n-1-i]

result = max(row_sum + column_sum + cross_sum)

print(result)


# solution2
max_value = -2147000000

for i in range(n):
    row_sum = column_sum = 0
    for j in range(n):
        row_sum += arr[i][j]
        column_sum += arr[j][i]

        if max(row_sum, column_sum) > max_value:
            max_value = max(row_sum, column_sum)

cross_sum1 = cross_sum2 = 0
for i in range(n):
    cross_sum1 += arr[i][i]
    cross_sum2 += arr[i][n-1-i]

if max(cross_sum1, cross_sum2) > max_value:
    max_value = max(cross_sum1, cross_sum2)

print(max_value)
