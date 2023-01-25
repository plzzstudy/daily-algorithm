# 평범한 배낭(https://www.acmicpc.net/problem/12865)
import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())

# dp 테이블 초기화
# dp[i][j] : j 무게에서 i번째 물건을 넣었을 때 최대 가치
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n + 1):  # 1 ~ N
    w, v = map(int, input().rstrip().split())

    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= w and dp[i - 1][j - w] + v > dp[i][j]:
            dp[i][j] = dp[i - 1][j - w] + v

print(dp[n][k])
