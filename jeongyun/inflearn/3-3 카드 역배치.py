import sys
# sys.stdin = open("input.txt", "r")
res = list(range(1, 21))
for i in range(10):
    a = list(map(int, input().split()))
    b = res[a[0]-1:a[-1]]
    b.reverse()
    res[a[0]-1:a[-1]] = b
for i in res:
    print(i, end=' ')
