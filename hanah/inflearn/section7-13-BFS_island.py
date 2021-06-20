'''
# 섬나라 아일랜드(BFS)

섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다. 
각 섬은 1로 표시되어 상하좌우와 대각선으로 연결되어 있으며, 0은 바다입니다. 
섬나라 아일랜드에 몇 개의 섬이 있는지 구하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다. 
두 번째 줄부터 격자판 정보가 주어진다.

▣ 출력설명
첫 번째 줄에 섬의 개수를 출력한다.

▣ 입력예제 1
7 
1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0

▣ 출력예제 1
5

'''

import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    arr[x][y] = 0
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)



