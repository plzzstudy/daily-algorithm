'''
# 조합 구하기

1부터N까지 번호가 적힌 구슬이 있습니다. 
이중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 
출력순서는 사전순으로 오름차순으로 출력합니다.

▣ 입력예제 1 
42

▣ 출력예제 1 
1 2
1 3
1 4
2 3 
2 4 
3 4 
6

'''

# solution1
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
cnt = 0

for nums in combinations(range(1, n+1), m):
    for num in nums:
        print(num, end=' ')
    cnt += 1
    print()

print(cnt)


# solution2
n, m = map(int, sys.stdin.readline().split())
cnt = 0
res = [0] * m

def dfs(L, ns): # ns는 다음 번에 for문 시작하는 수
    global cnt
    if L == m:
        for num in res:
            print(num, end=' ')
        cnt += 1
        print()
    else:
        for i in range(ns, n+1):
            res[L] = i
            dfs(L+1, i+1)

dfs(0, 1)
print(cnt)
