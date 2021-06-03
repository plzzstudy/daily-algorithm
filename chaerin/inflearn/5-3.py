# 후위표기식 만들기

# 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
# 중위표기식은 우리가 흔히 쓰는 표현식입니다. 
# 즉 3+5 와 같이 연산자가 피연산자 사이에 있으면 중위표기식입니다.
# 후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
# 예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
# 만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면
#(3+5)*2 이면 35+2* 로 바꾸어야 합니다.

# ▣ 입력설명
# 첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다. 
# 식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.

# ▣ 출력설명 
# 후위표기식을 출력한다.

a=input()
stack=[]
result=''

for i in a:
    if i.isdecimal():
        result+=i
    else:
        if i=='(':
            stack.append(i)
        elif i=='*' or i=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                result+=stack.pop()
            stack.append(i)
        elif i=='+' or i=='-':
            while stack and stack[-1]!='(':
                result+=stack.pop()
            stack.append(i)
        elif i==')':
            while stack and stack[-1]!='(':
                result+=stack.pop()
            stack.pop()
while stack:
    result+=stack.pop()

print(result)