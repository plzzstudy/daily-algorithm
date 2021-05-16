# 격자판 최대합

# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중
# 가장 큰 합을 출력합니다.

N = int(input())
sqr = [list(map(int, input().split())) for _ in range(N)]

a = [sum(sqr[i]) for i in range(N)] + \
    [sum(i) for i in zip(*sqr)] + \
    [sum([sqr[i][i] for i in range(N)])] + \
    [sum([sqr[i][-(i+1)] for i in range(N)])]

a.sort()
print(a[-1])


# solution
largest = -2147000000

# 직선방향
for i in range(N):
    sum1 = sum2 =0
    for j in range(N):
        sum1 += sqr[i][j]
        sum2 += sqr[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0

# 대각선방향
for i in range(N):
    sum1 += sqr[i][i]
    sum2 += sqr[i][N-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)