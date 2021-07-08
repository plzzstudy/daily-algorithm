# 동전분배하기

# N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다.
# 세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 
# 총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
# 단 세 사람의 총액은 서로 달라야 합니다.

def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha

    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]

if __name__=="__main__":
    n=int(input())
    coin=[]
    money=[0]*3     # 세 사람
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)