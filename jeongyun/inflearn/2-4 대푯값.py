import sys
# sys.stdin=open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a)/n)
b = []
for i in a:
    b.append(avg-i)
c = []
for i in b:
    c.append(abs(i))
d = min(c)
e = []
for i in range(n):
    if c[i] == d:
        e.append(i)
f = 0
g = 0
for i in e:
    if f < a[i]:
        f = a[i]
        g = i
    if f == a[i]:
        pass
print(avg, g+1)
