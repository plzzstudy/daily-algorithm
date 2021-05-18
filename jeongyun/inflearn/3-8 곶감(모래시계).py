import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:  # 왼쪽으로 회전하는 경우
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:  # 오른쪽으로 회전하는 경우
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
# for x in a:
#     print(x)
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n // 2:  # 좁혀들어간다
        s += 1
        e -= 1
    else:  # 다시 넓혀나간다
        s -= 1
        e += 1
print(res)
