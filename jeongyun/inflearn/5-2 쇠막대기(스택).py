import sys
# sys.stdin = open("input.txt", "r")
s = input()
stk = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stk.append(s[i])
    else:
        stk.pop()
        if s[i-1] == '(':
            # stk.pop()
            cnt += len(stk)
        else:
            # stk.pop()
            cnt += 1
print(cnt)
