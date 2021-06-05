'''
# 음료수 얼려먹(DFS, BFS 기초)

N x M크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

- 입력 조건
첫번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N,M <= 1000)
두 번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

- 출력 조건
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

- 입력 예시
4 5
00110
00011
11111
00000

- 출력 예시
3

'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# solution1 - BFS

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # graph 범위를 벗어날 경우 이 nx, ny는 건너 뜀
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 다음 노드가 0일 경우만 탐색 진행
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1 # 방문처리
                q.append((nx, ny))

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)

    

# solution2 - DFS
def dfs(x, y):
    # 범위를 벗어나면 즉시 종료(return False)
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True # 탐색 종료
    return False # 0이 아닌 곳은 바로 False 리턴


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j): # 처음 방문한 노드가 0이라면 cnt 증가(연결된 노드는 어차피 한꺼번에 탐색되므로 True는 처음 방문한 곳 하나만 있으면 됨)
            cnt += 1

print(cnt)

    
