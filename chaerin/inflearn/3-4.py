# 두 리스트 합치기

# 오름차순으로 정렬된 두 리스트가 주어지면
# 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

plus = N + M
plus.sort()
for i in plus:
    print(i, end='')


# solution
p1 = p2 = 0
a = []
while p1 < n and p2 < m:
    if N[p1]<=M[p2]:
        a.append(N[p1])
        p1 += 1
    else:
        a.append(M[p2])
        p2 += 1
if p1 < n:
    a = a + N[p1:]
if p2 < m:
    a = a + M[p2:]

for i in a:
    print(i, end='')