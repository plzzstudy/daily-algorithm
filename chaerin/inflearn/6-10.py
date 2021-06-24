# 조합 구하기

# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하세요.

def DFS(L, s):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        cnt+=1
        print()
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*(m+1)
    cnt=0
    DFS(0, 1)
    print(cnt)