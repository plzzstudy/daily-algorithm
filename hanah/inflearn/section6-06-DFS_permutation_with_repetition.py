'''
# 중복순열

1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력합니다.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
출력순서는 사전순으로 오름차순으로 출력합니다.

▣ 입력예제 1 
32

▣ 출력예제 1 
1 1
1 2
1 3
2 1 
2 2 
2 3 
3 1 
3 2 
3 3 
9

'''

# solution1 - 내장 모듈 이용
from itertools import product

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
cnt = 0
for x in product(nums, repeat=m):
    for num in x:
       print(num, end=' ')
    print()
    cnt += 1
print(cnt)


# solution2 - DFS
n, m = map(int, input().split())
cnt = 0
result = [0] * m

def dfs(L):
    global cnt
    if L == m:
        for a in result:
            print(a, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            result[L] = i
            dfs(L + 1)

dfs(0)
print(cnt)
