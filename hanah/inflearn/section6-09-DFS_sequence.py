'''
# 수열 추측하기

가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다. 
그리고 둘째 줄부터 차례대로 파스칼 의 삼각형처럼 위의 두개를 더한 값이 저장되게 된다. 
예를 들어 N이 4 이고 가장 윗 줄에 3 1 2 4 가 있다고 했을 때, 다음과 같은 삼각형이 그려진다.

 3 1 2 4 
  4 3 6 
   7 9 
   16
N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램을 작성하시오. 
단, 답이 여러가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력하여야 한다.

▣ 입력설명
첫째 줄에 두개의 정수 N(1≤N≤10)과 F가 주어진다.
N은 가장 윗줄에 있는 숫자의 개수를 의미하며 F는 가장 밑에 줄에 있는 수로 1,000,000 이하이다.

▣ 출력설명
첫째 줄에 삼각형에서 가장 위에 들어갈 N개의 숫자를 빈 칸을 사이에 두고 출력한다. 
답이 존재 하지 않는 경우는 입력으로 주어지지 않는다.

▣ 입력예제 1 
4 16

▣ 출력예제 1 
3 1 2 4

'''

# solution1
from math import factorial
from itertools import permutations

n, f = map(int, input().split())
b = [1] * n # 이항계수 초기화(맨 앞과 맨 뒤는 무조건 1이라서 1로 초기화)
for i in range(1, n):
    b[i] = factorial(n-1) // (factorial(n-1-i) * factorial(i)) # nCr >> 외우기...

for nums in permutations(range(1, n+1), r=n):
    sum = 0
    for i, num in enumerate(nums):
        sum += num * b[i]
    
    if sum == f:
        for num in nums:
            print(num, end=' ')
        break


# solution2
import sys

n, f = map(int, input().split())
b = [1] * n 
for i in range(1, n):
    b[i] = b[i-1] * (n-i) // i  # DP방식(더 빠름)

result = [0] * n # 순열
check = [0] * (n+1) # 순열에 중복된 수가 없도록 체크

def dfs(L, sum):
    if L == n and sum == f:
        for num in result:
            print(num, end=' ')
        sys.exit(0)

    else:
        for i in range(1, n+1): # 1 ~ n까지 순열 구하기
            if check[i] == 0: # 아직 순열에 안 쓰인 수라면
                check[i] = 1
                result[L] = i
                dfs(L+1, sum + (result[L] * b[L]))
                check = 0

dfs(0, 0)


