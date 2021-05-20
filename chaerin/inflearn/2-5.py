# 정다면체

# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
# 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

N, M = map(int, input().split())

sum = []
for i in range(N):
    for j in range(M):
        sum.append((i+1)+(j+1))

cnt = 0
for i in list(set(sum)):
    if cnt < sum.count(i):
        cnt = sum.count(i)

for i in list(set(sum)):
    if cnt == sum.count(i):
        print(i, end=' ')



# solution
cnt = [0]*(N+M+3)
max = -2147000000

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1

for i in range(N+M+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(N+M+1):
    if cnt[i] == max:
        print(i, end=' ')