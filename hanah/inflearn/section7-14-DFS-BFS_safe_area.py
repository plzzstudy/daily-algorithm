'''
# 안전영역(BFS, DFS)

재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다.
먼저 어떤 지역의 높이 정보를 파악한다.
그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다.

이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.

어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 
배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다. 
예를 들어, 다음은 N=5인 지역의 높이 정보이다.

6 8 2 6 2
3 2 3 4 6 
6 7 3 3 2 
7 2 5 3 6  
8 9 5 2 7

이제 위와 같은 지역에 많은 비가 내려서 높이가 4 이하인 모든 지점이 물에 잠겼다고 하자.
물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며
그 크기가 최대인 영역을 말한다. 
위의 경우에서 물에 잠기지않는 안전한 영역은 5개가 된다(꼭지점으로만 붙어있는 두 지점은 인접하지 않는다고 취급한다). 

또한 위와 같은 지역에서 높이가 6이하인 지점을 모두 잠기게 만드는 많은 비가 내리면 
물에 잠기지 않는 안전한 영역은 4개가 된다.

이와 같이 장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다. 
위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해보면 
물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.


어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하라.


▣ 입력설명
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. 
N은 2 이상 100 이하의 정수이다. 
둘째 줄부터 N 개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N 개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다.
높이는 1이상 100 이하의 정수이다.

▣ 출력설명
첫째 줄에 장마철에 물에 잠기지 않는 안전한영역의 최대 개수를 출력한다.

▣ 입력예제 1 
5
6 8 2 6 2
3 2 3 4 6 
6 7 3 3 2 
7 2 5 3 6  
8 9 5 2 7


▣ 출력예제 1 
5

'''

# solution1 - BFS
import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
heights = []
for i in range(n):
    for j in range(n):
        if arr[i][j] not in heights:
            heights.append(arr[i][j])        

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, h, check):
    q = deque()
    q.append((a, b))
    check[a][b] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > h and check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append((nx, ny))


max_cnt = 0
for h in heights:
    cnt = 0
    check = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and check[i][j] == 0:
                bfs(i, j, h, check)
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)


# solution2
def dfs(x, y, h, check):
    check[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0 and arr[nx][ny] > h:
            dfs(nx, ny, h, check)


max_cnt = 0
for h in heights:
    check = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and check[i][j] == 0:
                dfs(i, j, h, check)
                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)


