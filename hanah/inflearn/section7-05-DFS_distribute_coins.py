'''
# 동전 분배하기(DFS)

N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다.
세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 
총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.

단 세 사람의 총액은 서로 달라야 합니다.

▣ 입력설명
첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다.
그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.

▣ 출력설명 
총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.

▣ 입력예제 1
7
8
9
11 
12 
23 
15 
17

▣ 출력예제 1
5

해설 : 29(12+17), 32(8+9+15), 34(11+23) 로 분배하면 최대금액과 최소금액의 차가 5가 되어 5가 최소차가 된다.

'''

import sys

n = int(sys.stdin.readline().rstrip())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
check = [0] * n
min_v = 2147000000
abc = [0, 0, 0]

def dfs(L, abc):
    global min_v
    if L == n:
        if len(set(abc)) != 3:
            return
        else:
            diff = max(abc) - min(abc)
            if diff < min_v:
                min_v = diff
        
    else:
        for i in range(3):
            abc[i] += coins[L]
            dfs(L+1, abc)
            abc[i] -= coins[L]

dfs(0, abc)
print(min_v)

