# 휴가

# 카운셀러로 일하고 있는 현수는 오늘부터 N+1일째 되는 날 휴가를 가기 위해서, 
# 남은 N일 동안 최대한 많은 상담을 해서 휴가비를 넉넉히 만들어 휴가를 떠나려 한다.
# 현수가 다니는 회사에 하루에 하나씩 서로 다른 사람의 상담이 예약되어 있다.
# 각각의 상담은 상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P로 이루어져 있다.

# 현수가 휴가를 가기 위해 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    T=list()    # 상담을 완료하는데 걸리는 날 수
    P=list()    # 상담을 했을 때 받을 수 있는 금액
    for i in range(n):
        a, b=map(int, input().split())
        T.append(a)
        P.append(b)
    res=-2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)