'''
# 순열

1부터N까지번호가적힌구슬이있습니다.이중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 
출력순서는 사전순으로 오름차순으로 출력합니다.

▣ 입력예제 1 
32

▣ 출력예제 1 
1 2
1 3
2 1
2 3 
3 1 
3 2 
6

'''

import sys

# solution1 
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
cnt = 0
for nums in permutations(range(1, n+1), m):
    for num in nums:
        print(num, end=' ')
    print()
    cnt += 1
print(cnt)


# solution2 - DFS
n, m = map(int, sys.stdin.readline().split())
cnt = 0
res = [0] * m
check = [0] * (n+1) # 중복 체크 용도. 0이면 아직 안나온거

def dfs(L):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        cnt += 1
        print()
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1 
                res[L] = i
                dfs(L+1)
                check[i] = 0 # 돌아오면 다시 0으로 초기화
dfs(0)
print(cnt)
