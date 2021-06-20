# 중복순열 구하기

# 1부터 N까지 번호가 적힌 구슬이 있습니다. 
# 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다. 

import sys

input=sys.stdin.readline

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)