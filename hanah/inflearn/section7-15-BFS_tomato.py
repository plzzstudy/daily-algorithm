'''
# 토마토(BFS)

현수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
토마토는 아래의 그림 과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 

하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향 에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.

현수는 창고에 보관된 토마토들이 며칠이 지나 면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로 그램을 작성하라.

단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.


▣ 입력설명
첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다.
M은 상자의 가로 칸의 수, N 은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M, N ≤ 1,000 이다.

둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
즉, 둘째 줄부터 N개의 줄 에는 상자에 담긴 토마토의 정보가 주어진다. 
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

▣ 출력설명
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

▣ 입력예제 1
6 4
0  0 -1  0  0  0
0  0  1  0 -1  0
0  0 -1  0  0  0
0  0  0  0 -1  1

▣ 출력예제 1
4

'''

import sys
from collections import deque

# solution 1
m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

day = 1
while q:
    for i in range(len(q)):
        x, y = q.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = day
                q.append((nx, ny))
                
    day += 1

res = 0
check_zero = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            check_zero = 1
            print(-1)
            sys.exit(0)

        if arr[i][j] > res:
            res = arr[i][j]            

if res == 1:
    print(0)
else:
    print(res)




# solution2
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, input().split())) for _ in range(m)]
dis = [[0]*n for _ in range(m)]

q = deque()
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = 1
            dis[nx][ny] = dis[x][y]+1
            q.append((nx, ny))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            flag = 0

result = 0
if flag == 1: # 0이 하나도 없는 경우
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
