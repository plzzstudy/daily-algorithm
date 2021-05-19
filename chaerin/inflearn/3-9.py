# 봉우리

# 지도 정보가 N*N 격자판에 주어집니다. 
# 각 격자에는 그 지역의 높이가 쓰여있습니다. 
# 각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 
# 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.

n = int(input())
a = [[0]*(n+2)]*(n+2)

cnt = 0
b = []
for i in range(1, n+1):
    a[i] = [0] + list(map(int, input().split())) + [0]

for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and \
            a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]:
            cnt += 1
            b.append(a[i][j])
print(cnt)


# solution
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): # all():iterable 내의 모든 요소가 참이면 True
            cnt += 1
print(cnt)