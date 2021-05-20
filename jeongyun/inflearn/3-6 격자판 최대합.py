import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
max = 0
for i in range(n):
    if sum(a[i]) > max:
        max = sum(a[i])
# print(max)
c = []
for i in range(n):
    sum = 0
    for j in range(n):
        sum += a[j][i]
    if sum > max:
        max = sum
# print(max)
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > max:
    max = sum1
if sum2 > max:
    max = sum2
print(max)
