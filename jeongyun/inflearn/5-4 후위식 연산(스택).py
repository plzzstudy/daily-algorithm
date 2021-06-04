import sys
# sys.stdin = open("input.txt", "r")
a = input()
stk = []
for x in a:
    if x.isdecimal():
        stk.append(x)
    else:
        res = 0
        if x == '*':
            res = int(stk[-2]) * int(stk[-1])
        elif x == '/':
            res = int(stk[-2]) / int(stk[-1])
        elif x == '+':
            res = int(stk[-2]) + int(stk[-1])
        elif x == '-':
            res = int(stk[-2]) - int(stk[-1])
        stk.pop()
        stk.pop()
        stk.append(res)
print(stk[0])
