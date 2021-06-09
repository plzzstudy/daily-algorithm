import sys
# sys.stdin = open("input.txt", "r")
w1 = input()
d1 = {}
w2 = input()
d2 = {}
for x in w1:
    if x not in d1:
        d1[x] = w1.count(x)
for y in w2:
    if y not in d2:
        d2[y] = w2.count(y)
if d1 == d2:
    print("YES")
else:
    print("NO")
