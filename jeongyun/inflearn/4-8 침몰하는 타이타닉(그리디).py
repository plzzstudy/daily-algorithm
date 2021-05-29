import sys
# sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0
for i in range(n):
    if len(a) == 0:
        break
    elif len(a) == 1:
        cnt += 1
        a.pop()
        break
    elif a[0] + a[-1] <= m:
        cnt += 1
        a.pop()
        a.pop(0)
    else:
        cnt += 1
        a.pop()

print(cnt)
