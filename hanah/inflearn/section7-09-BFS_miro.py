'''
# 미로의 최단거리 통로 (BFS 활용)

7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력하는 프로그램을 작성하세요.
경로수는 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다. 
출발점은 격자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 
격자판의 1은 벽이고, 0은 도로이다.
격자판의 움직임은 상하좌우로만 움직인다. 

미로가 다음과 같다면

s 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 e

(s는 출발, e는 도착 지점)

위와 같은 경로가 최단 경로이며 경로수는 12이다.

▣ 입력설명
7*7 격자판의 정보가 주어집니다.

▣ 출력설명
첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.

▣ 입력예제 1
0 0 0 0 0 0 0 
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0

▣ 출력예제 1 
12

'''

import sys
from collections import deque

arr = [list(map(int, sys.stdin.readline().rstrip().split())) * 7 for _ in range(7)]
arr[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    if x == 6 and y == 6:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 7 and 0 <= ny <= 7:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


if arr[6][6] == 0:
    print(-1)
else:
    print(arr[6][6] - 1)


