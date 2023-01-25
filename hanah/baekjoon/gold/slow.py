
n, k = map(int, input().split())

# dp 테이블 초기화
# dp[i][j] : j 무게에서 i번째 물건을 넣었을 때 최대 가치
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n + 1):
    w, v = map(int, input().split())

    for j in range(1, k + 1):
        if j < w:  # 못 넣음 >> 이전 개수에서의 최대 가치 유지
            dp[i][j] = dp[i - 1][j]
        else:  # 넣거나 안넣거나
            # 안 넣었을 때(=이번 꺼를 안넣었을 때의 최대 가치)와 
            # 넣었을 때(=무게가 w인 것을 넣어야 하니까 이전 개수에서 j-w 무게였을 때 최대 가치에서 현재 가치를 더한 값을 비교해야 함)
            # 중에서 더 큰 값
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
