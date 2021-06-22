# 순열 구하기

# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.

def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
           print(result[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if check[i]==0:
                check[i]=1
                result[L]=i
                DFS(L+1)
                check[i]=0


if __name__=="__main__":
    n, m=map(int, input().split())
    result=[0]*n
    check=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)