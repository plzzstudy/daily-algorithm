'''
# 휴가가기 전 돈 모으기 (DFS)

카운셀러로 일하고 있는 현수는 오늘부터 N+1일째 되는 날 휴가를 가기 위해서, 
남은 N일 동 안 최대한 많은 상담을 해서 휴가비를 넉넉히 만들어 휴가를 떠나려 한다.

현수가 다니는 회사에 하루에 하나씩 서로 다른 사람의 상담이 예약되어 있다.
각각의 상담은 상담을 완료하는데 걸리는 날 수 T와 
상담을 했을 때 받을 수 있는 금액 P로 이 루어져 있다.

만약 N = 7이고, 아래와 같이 예약이 잡혔있다면

   | 1일 2일 3일 4일 5일 6일 7일
 T |  4   2   3   3   2   2   1
 P | 20  10  15  20  30  20  10

1일에 잡혀있는 상담은 총 4일이 걸리며, 상담했을 때 받을 수 있는 금액은 20이다.
만약 1일 에 예약된 상담을 하면 4일까지는 상담을 할 수가 없다.

하나의 상담이 하루를 넘어가는 경우가 많기 때문에 현수는 예약된 모든 상담을 혼자 할 수 없어 최대 이익이 나는 상담 스케쥴을 짜기로 했다.
휴가를 떠나기 전에 할 수 있는 상담의 최대 이익은 1일, 5일, 7일에 있는 상담을 하는 것이며, 
이때의 이익은 20+30+10=60이다.

현수가 휴가를 가기 위해 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

▣ 입력설명
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 1일부터 N일까지 순서대로 주어진다. (1 ≤ T ≤ 7, 1 ≤ P ≤ 100)

▣ 출력설명
첫째 줄에 현수가 얻을 수 있는 최대 이익을 출력한다.

▣ 입력예제 1 
7
4 20
2 10
3 15
3 20 
2 30 
2 20 
1 10

▣ 출력예제 1 
60

'''

import sys

n = int(sys.stdin.readline().rstrip())
c = [[0,0]] # 인덱스 0은 사용하지 않는 용도. c의 인덱스 = 날짜(1: 1일차,,,)
for _ in range(n):
    c.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_v = 0

def dfs(L, sum_money):
    global max_v
    if L == n+1: # n일 까지는 일 가능(n일에 1일이 필요한 일이라면 가능)
        if sum_money > max_v:
            max_v = sum_money
    else:
        if L+c[L][0] <= n+1:
            dfs(L+c[L][0], sum_money + c[L][1]) # L일에 상담하고 다음 상담일로 이동
        dfs(L+1, sum_money) # 이번 상담은 건너뛰고 다음날로 이동
        

dfs(1, 0)
print(max_v)
