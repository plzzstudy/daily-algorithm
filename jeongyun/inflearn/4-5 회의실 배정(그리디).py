import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x[1], x[0]))

cnt = 1
e = a[0][-1]

for i in range(1, n):
    if a[i][0] >= e:
        e = a[i][-1]
        cnt += 1

print(cnt)
