import sys
# sys.stdin = open("input.txt", 'rt')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n):
    a[i].insert(0, 0)
    a[i].append(0)
# print(a)
a.insert(0, [0]*(n+2))
a.append([0]*(n+2))
# print(a)
cnt = 0
for i in range(1, n+1):
    # print('i:', i)
    for j in range(1, n+1):
        # print('a[i][j]:', a[i][j])
        if (a[i][j] > a[i-1][j]) and (a[i][j] > a[i][j-1]) and (a[i][j] > a[i][j+1]) and (a[i][j] > a[i+1][j]):
            cnt += 1
print(cnt)
