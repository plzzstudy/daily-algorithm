import sys
# sys.stdin=open("input.txt", "rt")
nn=input()
n = int(nn.split()[0])
k = int(nn.split()[-1])
a = []
for i in range(1, n+1):
    if n % i == 0:
        a.append(i)
        i += 1
if len(a) < k:
    print(-1)
else:
    print(a[k-1])