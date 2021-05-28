import sys
# sys.stdin = open("input.txt", "r")
L = int(input())
a = list(map(int, input().split()))
m = int(input())
for i in range(m):
    highest = a.index(max(a))
    lowest = a.index(min(a))
    a[highest] -= 1
    a[lowest] += 1
print(max(a)-min(a))
