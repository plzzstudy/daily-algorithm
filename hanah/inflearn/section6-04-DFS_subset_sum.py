'''
# 합이 같은 부분집합(DFS)

N개의 원소로 구성된 자연수 집합이 주어지면, 
이 집합을 두 개의 부분집합으로 나누었을 때 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고,
그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.

둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어 합니다.

예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이 16으로 같은 경우가 존재하는 것을 알 수 있다.

▣ 입력설명
첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
두 번째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.

▣ 출력설명
첫 번째 줄에 “YES" 또는 ”NO"를 출력한다.

▣ 입력예제 1 
6
1 3 5 6 7 10

▣ 출력예제 1 
YES

'''

import sys

# solution1
# def dfs(i):
#     if i == n:
#         sum1 = sum([a[j] for j in range(i) if check[j]==1])
#         sum2 = total - sum1
#         if sum1 == sum2:
#             print('YES')
#             sys.exit(0) # 한번이라도 YES가 나오면 프로그램 종료
#     else:
#         check[i] = 1
#         dfs(i + 1)
#         check[i] = 0
#         dfs(i + 1)

# n = int(input())
# a = list(map(int, input().split()))
# check = [0] * (n)
# total = sum(a)
# dfs(0)

## 위에서 YES가 출력되지 않았다면 프로그램이 종료되지 않은 경우이므로 이 경우 NO를 출력
# print('NO')


# solution2 (더 빠름)
def dfs(L, sum): # L은 레벨을 의미(=a리스트의 index), sum은 지금까지의 부분집합의 합
    if sum > (total // 2): # 한 부분집합의 sum이 total의 절반보다 커져버리면 이미 sum1==sum2는 성립하지 않으므로 패스(시간단축)
        return

    if L == n:
        if sum == (total - sum):
            print('YES')
            sys.exit(0)
    else:
        dfs(L+1, sum + a[L]) # 현재 수(=a[L])를 부분집합에 포함
        dfs(L+1, sum) # 현재 수를 부분집합에 포함하지 않음

n = int(input())
a = list(map(int, input().split()))
total = sum(a)
dfs(0, 0)
print('NO')

