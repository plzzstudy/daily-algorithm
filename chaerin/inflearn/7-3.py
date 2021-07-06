# 양팔저울

# 무게가 서로 다른 K개의 추와 빈 그릇이 있다. 
# 모든 추의 무게는 정수이고, 그릇의 무게는 0 으로 간주한다. 
# 양팔저울을 한 번만 이용하여 원하는 물의 무게를 그릇에 담고자 한다.
# 주어진 모든 추 무게의 합을 S라 하자.

# K(3<=K<=13)개의 추 무게가 주어지면, 1부터 S사이의 정수 중 
# 측정이 불가능한 물의 무게는 몇 가지가 있는지 출력하는 프로그램을 작성하세요.

def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())  # 추의 개수
    G=list(map(int, input().split()))    # 각 추의 무게들
    s=sum(G)    # 추 무게의 총합
    res=set()
    DFS(0, 0)
    print(s-len(res))