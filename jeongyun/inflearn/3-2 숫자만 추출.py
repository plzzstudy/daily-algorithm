import sys
# sys.stdin = open("input.txt", "rt")
a = input()
b = ''
c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in a:
    if i in c:
        b = b + i
b = int(b)
print(b)
d = 0
for i in range(1, b+1):
    if b % i == 0:
        d += 1
print(d)
