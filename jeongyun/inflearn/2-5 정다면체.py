import sys
# sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = []
for i in range(1, n+1):
    for j in range(1, m+1):
        a.append(i+j)
c = []
for i in a:
    c.append(a.count(i))
e = []
for i in a:
    if a.count(i) == max(c) and i not in e:
        e.append(i)
e.sort()
for i in e:
    print(i, end=' ')
