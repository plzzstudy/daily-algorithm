import sys
# sys.stdin = open("input.txt", 'rt')
n1 = int(input())
a = list(map(int, input().split()))
# print('a:', a)
n2 = int(input())
b = list(map(int, input().split()))
# print('b:', b)
c = []
p1 = 0
p2 = 0
while p1 < n1 or p2 < n2:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
    if p1 == n1:
        c = c + b[p2:]
        break
    elif p2 == n2:
        c = c + a[p1:]
        break
# print(c)
for i in c:
    print(i, end=' ')
