'''
# 등산 경로(DFS)

등산을 매우 좋아하는 철수는 마을에 있는 뒷산에 등산경로를 만들 계획을 세우고 있습니다. 
마을 뒷산의 형태를 나타낸 지도는 N*N 구역으로 나뉘어져 있으며, 각 구역에는 높이가 함께 나타나 있습니다.
N=5이면 아래와 같이 표현됩니다.

 2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100

어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동할 수 있도록 등산로를 설계하려고 합니다. 
등산로의 출발지는 전체 영역에서 가장 낮은 곳이고, 목적지는 가장 높은 곳입니다. 
출발지와 목적지는 유일합니다. 
지도가 주어지면 출발지에서 도착지로 갈 수 있는 등산 경로가 몇 가지 인지 구하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 N(5<=N<=13)주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.

▣ 출력설명
등산경로의 가지수를 출력한다.

▣ 입력예제 1
5
2  23 92 78 93 
59 50 48 90 80 
30 53 70 75 96
94 91 82 89 93 
97 98 95 96 100

▣ 출력예제 1
5

'''

import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_v = 2147000000
max_v = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] < min_v:
            min_v = arr[i][j]
            sx, sy = i, j
        if arr[i][j] > max_v:
            max_v = arr[i][j]
            ex, ey = i, j

check = [[0] * n for _ in range(n)]
cnt = 0
def dfs(x, y):
    global cnt

    if x == ex and y == ey:
        cnt += 1
    
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > arr[x][y] and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    dfs(nx, ny)
                    check[nx][ny] = 0


dfs(sx, sy)
print(cnt)
