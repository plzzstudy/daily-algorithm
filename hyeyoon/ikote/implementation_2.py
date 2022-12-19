"""
시각: 완전 탐색
"""
n = int(input())

# 00시00분 00초 ~ 01시 59분 59초
cnt = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
