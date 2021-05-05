import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(input().split())

c = []


def digit_sum(x):
    b = 0
    for j in x:
        b = b + int(j)
    return b


for x in a:
    sum = digit_sum(x)
    c.append(sum)
print(a[(c.index(max(c)))])
