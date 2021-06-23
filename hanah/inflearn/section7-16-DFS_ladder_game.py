'''
# 사다리 타기(DFS)

현수와 친구들은 과자를 사먹기 위해 사다리 타기를 합니다.
사다리 표현은 2차원 평면은 0으로 채워지고, 사다리는 1로 표현합니다. 
현수는 특정 도착지점으로 도착하기 위해서는 몇 번째 열에서 출발해야 하는지 알고싶습니다. 
특정 도착지점은 2로 표기됩니다. 여러분이 도와주세요.

▣ 입력설명
10*10의 사다리 지도가 주어집니다.

▣ 출력설명
출발지 열 번호를 출력하세요.

▣ 입력예제 1 
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1 
1 0 1 0 0 1 0 1 0 1 
1 0 1 0 0 1 0 1 1 1 
1 0 1 0 0 1 0 1 0 1 
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1 
1 1 1 0 0 1 0 1 0 1 
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1

▣ 출력예제 1 
7

'''
import sys
sys.stdin=open("input.txt", "r")
def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


board=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
for y in range(10):
    if board[9][y]==2:
        DFS(9, y)
