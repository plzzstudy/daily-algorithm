import sys
# sys.stdin = open("input.txt", "r")
num, m = map(int, input().split())
num = list(map(int, str(num)))
stk = []
for x in num:
    while stk and m > 0 and stk[-1] < x:
        stk.pop()
        m -= 1
    stk.append(x)
if m != 0:
    stk = stk[:-m]
res = ''.join(map(str, stk))
print(res)
