'''
# 플로이드 워샬 알고리즘

N개의 도시가 주어지고, 각 도시들을 연결하는 도로와 해당 도로를 통행하는 비용이 주어질 때 
모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최소값을 구하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에는 도시의 수N(N<=100)과 도로수 M(M<=200)가 주어지고,
M줄에 걸쳐 도로정보 와 비용(20 이하의 자연수)이 주어진다.
만약 1번 도시와 2번도시가 연결되고 그 비용이 13이 면 “1 2 13”으로 주어진다.

▣ 출력설명
모든 도시에서 모든 도시로 이동하는데 드는 최소 비용을 아래와 같이 출력한다.
자기자신으로 가는 비용은 0입니다. 
i번 정점에서 j번 정점으로 갈 수 없을 때는 비용을 “M"으 로 출력합니다.

▣ 입력예제 1
5 8 
1 2 6 
1 3 3
3 2 2 
2 4 1 
2 5 13 
3 4 5
4 2 3 
4 5 7

▣ 출력예제 1
0 5 3 6 13 //1번 정점에서 2번정점으로 5, 1에서 3번 정점으로 3, 1에서 4번 정점으로 6......
M 0 M 1 8 //2번 정점에서 1번 정점으로는 갈수 없으므로 “M", .......
M 2 0 3 10
M 3 M 0 7
M M M M 0

'''
import sys

n, m = map(int, sys.stdin.readline().split())

# 인접행렬로 dp테이블 초기화
dp = [[20000] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = 0

for i in range(m):
    a, b, x = map(int, sys.stdin.readline().rstrip().split())
    dp[a][b] = x

# print(dp)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1): 
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]) 
            # i->j를 가는 방법 중 i, j가 바로 연결되 있는 경우랑, 어디를 거쳐서 오는 경우 중 적은 것으로
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == 20000:
            print("M", end=' ')
        else:
            print(dp[i][j], end=' ')
    print()
