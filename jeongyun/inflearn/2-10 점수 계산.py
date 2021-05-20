import sys
# sys.stdin = open("input.txt", "rt")
N = int(input())
a = list(map(int, input().split()))
b = 0
c = []
for i in range(N):
    if a[i] == 0:
        b = 0
        c.append(b)
    elif a[i] == 1:
        b = b + 1
        c.append(b)
print(sum(c))
