# 후위식 연산

# 후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
# 만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.

a=input()
stack=[]

for i in a:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i=='+':
            stack.append(stack.pop(-2)+stack.pop())
        elif i=='-':
            stack.append(stack.pop(-2)-stack.pop())
        elif i=='*':
            stack.append(stack.pop(-2)*stack.pop())
        elif i=='/':
            stack.append(stack.pop(-2)/stack.pop())

print(stack[0])