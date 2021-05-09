import sys
# sys.stdin = open("input.txt", "rt")
N = int(input())
b = []
for n in range(N):
    a = list(map(int, input().split()))
    result = 0
    for i in a:
        if a.count(i) == 3:
            result = 10000 + i * 1000
        elif a.count(i) == 2:
            result = 1000 + i * 100
        else:
            result = max(a) * 100
    b.append(result)
print(max(b))
