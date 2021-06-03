'''
# 경로 탐색(그래프 DFS)

방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램을 작성하세요. 
아래 그래프에서 1번 정점에서 5번 정점으로 가는 가지 수는
1 2 3 4 5 
1 2 5
1 3 4 2 5
1 3 4 5
1 4 2 5 
1 4 5
총 6가지 입니다.

▣ 입력설명
첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다.
그 다음부터 M줄에 걸쳐 연 결정보가 주어진다.

▣ 출력설명
경로들을 모두 출력하고 총 가지수를 출력한다.

▣ 입력예제 1
5 9
1 2
1 3
1 4
2 1 
2 3 
2 5
3 4 
4 2 
4 5

▣ 출력예제 1 
1 2 3 4 5 
1 2 5
1 3 4 2 5
1 3 4 5
1 4 2 5 
1 4 5
6

'''

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [0] * (n+1) # 한번 방문한 노드는 다시 방문하지 않게 방문처리
matrix = [[0] * (n+1) for _ in range(n+1)]
nodes = [1]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    matrix[x][y] = 1

cnt = 0
def dfs(x):
    global cnt
    visited[x] = 1

    if x == n:
        cnt += 1
        for node in nodes:
            print(node, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if matrix[x][i] == 1 and visited[i] == 0:
                nodes.append(i)
                dfs(i)
                nodes.pop()
                visited[i] = 0 # 백 할때는 방문처리했던거를 다시 풀어줘야 함(다음 탐색을 위해서)

dfs(1)
print(cnt)
