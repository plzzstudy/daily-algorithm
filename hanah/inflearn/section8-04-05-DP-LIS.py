'''
# 최대 부분 증가수열(LIS: Longest Increasing Subsequence)

N개의 자연수로 이루어진 수열이 주어졌을 때, 
그 중에서 가장 길게 증가하는(작은 수에서 큰 수로) 원소들의 집합을 찾는 프로그램을 작성하라.

예를 들어, 원소가 2, 7, 5, 8, 6, 4, 7, 12, 3 이면 가장 길게 증가하도록 원소들을 차례대로 뽑아내면
2, 5, 6, 7, 12를 뽑아내어 길이가 5인 최대 부분 증가수열을 만들 수 있다.

▣ 입력설명
첫째 줄은 입력되는 데이터의 수 N(2≤N≤1,000, 자연수)를 의미하고, 
둘째 줄은 N개의 입력데이터들이 주어진다.

▣ 출력설명
첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.

▣ 입력예제 1
8 
5 3 7 8 6 2 9 4

▣ 출력예제 1 
4

'''
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


# solution1
dp = [1] * n # 각 인덱스까지의 가장 작은 부분 증가수열은 1이므로 1로 초기화

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# solution2
arr.insert(0,0)
dp = [0] * (n+1)
dp[1] = 1

res = 0

for i in range(2, n+1):
    max_v = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dp[j] > max_v:
            max_v = dp[j]
    dp[i] = max_v + 1

    if dp[i] > res:
        res = dp[i]

print(res)