import sys
# sys.stdin = open("input.txt", "r")
a = input()
stk = []
res = ''
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stk.append(x)
        elif x == '*' or x == '/':
            while stk and (stk[-1] == '*' or stk[-1] == '/'):
                res += stk.pop()
            stk.append(x)
        elif x == '+' or x == '-':
            while stk and stk[-1] != '(':
                res += stk.pop()
            stk.append(x)
        elif x == ')':
            while stk and stk[-1] != '(':
                res += stk.pop()
            stk.pop()
while stk:
    res += stk.pop()
print(res)
