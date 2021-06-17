'''
# 사과나무(BFS)

현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어져있다.
N의 크기는 항상 홀수이다. 
가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다.
  
10 13 |10| 12 15
12 |39 30 23| 11
|11 25 50 53 15|
19 |27 29 37| 27
19 13 |30| 13 19

현수과 수확하는 사과의 총 개수를 출력하세요.

▣ 입력설명
첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 
이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
각 격자안의 사과의 개수는 100을 넘지 않는다.

▣ 출력설명
수확한 사과의 총 개수를 출력합니다.

▣ 입력예제 1
5
10 13 10 12 15
12 39 30 23 11 
11 25 50 53 15 
19 27 29 37 27 
19 13 30 13 19

▣ 출력예제 1 
379

'''

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# BFS로 탐색하면 마름모 모양으로 탐색한다는 것을 이용

# 정 가운데 좌표를 시작점으로
x = y = n // 2 

q = deque()
q.append((x, y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = arr[x][y]
level = 0

visited = [[0] * n for _ in range(n)]
visited[x][y] = 1

while q:
    if level == n // 2:
        break
    
    size = len(q)
    
    for i in range(size):
        cur_x, cur_y = q.popleft()
        for j in range(4):
            nx = cur_x + dx[j]
            ny = cur_y + dy[j]

            if visited[nx][ny] == 0:  # 0이면
                visited[nx][ny] = 1
                total += arr[nx][ny]
                q.append((nx, ny))
    
    level += 1
    
print(total)
                






