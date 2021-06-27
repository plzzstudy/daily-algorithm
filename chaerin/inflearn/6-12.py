# 수열 추측하기

# 가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다. 
# 그리고 둘째 줄부터 차례대로 파스칼의 삼각형처럼 위의 두개를 더한 값이 저장되게 된다. 
# N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램을 작성하시오. 
# 단, 답이 여러가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력하여야 한다.

import itertools as it

n, f=map(int, input().split())
b=[1]*n
cnt=0

for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1, n+1))
for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break