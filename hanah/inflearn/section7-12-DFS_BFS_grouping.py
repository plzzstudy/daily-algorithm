'''
# 단지 번호 붙이기(DFS, BFS)

그림1과 같이 정사각형 모양의 지도가 있다.
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.

그림2는 그림1을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

[그림1]
0 1 1 0 1 0 0
0 1 1 0 1 0 1
1 1 1 0 1 0 1
0 0 0 0 1 1 1
0 1 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 0 0 0

[그림2]
0 1 1 0 2 0 0
0 1 1 0 2 0 2
1 1 1 0 2 0 2
0 0 0 0 2 2 2
0 3 0 0 0 0 0
0 3 3 3 3 3 0
0 3 3 3 0 0 0

▣ 입력설명
첫 번째줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력 되고 
그 다음 N줄에는 각각 N개의 자료(0 혹은 1)가 입력된다

▣ 출력설명
첫 번째줄에는 총 단지수를 출력하시오.
그리고 각 단지내의 집의 수를 오름차순으로 정렬하여 한줄에 하나씩 출력하시오

▣ 입력예제 1
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

▣ 출력예제 1
3 
7 
8 
9

'''

import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)] 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

group = 0

def bfs(a, b, cnt):
    q = deque()
    q.append((a, b))
    arr[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt

count = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            cnt = bfs(i, j, 1)
            group += 1
            count.append(cnt)

count.sort()
print(group)
for x in count:
    print(x)

            
