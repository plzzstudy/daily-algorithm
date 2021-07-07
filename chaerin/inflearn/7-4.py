# 동전바꿔주기

# 명보네 동네 가게의 현금 출납기에는 k가지 동전이 각각n1, n2, ... , nk개 씩 들어있다.
# 가게 주인은 명보에게 T원의 지폐를 동전으로 바꿔 주려고한다. 
# 이때, 동전 교환 방법은 여러 가지가 있을 수 있다.
# 예를 들어, 10원 짜리, 5원 짜리, 1원 짜리 동전이 각각2개, 3개, 5개씩 있을 때, 20원 짜리 지폐를 다음과 같은4가지 방법으로 교환할 수 있다.
# 20 = 10×2
# 20 = 10×1+5×2
# 20 = 10×1+5×1+1×5
# 20 = 5×3+1×5
# 입력으로 지폐의 금액 T, 동전의 가지수 k, 각 동전 하나의금액 pi와 개수 ni가 주어질 때 (i=1,2,...,k)
# 지폐를 동전으로 교환하는 방법의 가지 수를 계산하는프로그램을 작성하시오. 
# 방법의 수는 231 을 초과하지않는 것으로 가정한다.

def DFS(L, sum):
    global cnt
    if sum>T:
        return
    if L==k:
        if sum==T:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))

if __name__=="__main__":
    T=int(input())  # 지폐 금액
    k=int(input())  # 동전의 개수
    cv=list()   # 동전의 금액
    cn=list()   # 동전의 개수
    for i in range(k):
        a, b=map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt=0
    DFS(0, 0)
    print(cnt)