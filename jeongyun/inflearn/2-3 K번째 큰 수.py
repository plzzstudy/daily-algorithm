import sys
# sys.stdin=open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
d = []
for i in range(n):
    for j in range(i+1, n):
        if i == j:
            pass
        for m in range(i+2, n):
            if i == j or j == m:
                pass
            else:
                c = a[i]+a[j]+a[m]
            if c not in d:
                d.append(c)
d.sort(reverse=True)
print(d[k-1])
