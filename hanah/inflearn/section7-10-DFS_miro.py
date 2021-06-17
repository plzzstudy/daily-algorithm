'''
# 미로탐색(DFS)

7*7 격자판 미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요.
출발점은 격자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 
격자판의 1은 벽이고, 0은 통로이다. 격 자판의 움직임은 상하좌우로만 움직인다.
미로가 다음과 같다면

s 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 e

(s는 출발, e는 도착 지점)

▣ 입력설명
7*7 격자판의 정보가 주어집니다.

▣ 출력설명
첫 번째 줄에 경로의 가지수를 출력한다.

▣ 입력예제 1
0 0 0 0 0 0 0
0 1 1 1 1 1 0 
0 0 0 1 0 0 0 
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0 
1 0 0 0 0 0 0

▣ 출력예제 1 
8

'''
import sys

arr = [list(map(int, sys.stdin.readline().rstrip().split())) * 7 for _ in range(7)]
arr[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
def dfs(x, y):
    global cnt

    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 7 and 0 <= ny < 7 and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                dfs(nx, ny)
                arr[nx][ny] = 0

dfs(0, 0)
print(cnt)


