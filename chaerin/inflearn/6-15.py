# 경로 탐색(그래프 DFS)

# 방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 
# 모든 경로의 가지 수를 출력하는 프로그램을 작성하세요.

def DFS(v):
    global cnt
    if v==n:
        cnt+=1
        # for x in path:            # 가지 수 케이스
        #     print(x, end=' ')
        # print()
    else:
        for i in range(1, n+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0

if __name__=="__main__":
    n, m=map(int, input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for i in range(m):
        a, b=map(int, input().split())
        g[a][b]=1
    cnt=0
    path=[]
    path.append(1)
    ch[1]=1
    DFS(1)
    print(cnt)