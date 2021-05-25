'''
# 후위표기식

중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있으면 중위표기식입니다.
후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.

예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면
(3+5)*2 이면 35+2* 로 바꾸어야 합니다.

▣ 입력설명
첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다. 식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.

▣ 출력설명 
후위표기식을 출력한다.

▣ 입력예제 1 
3+5*2/(7-2)

▣ 출력예제 1 
352*72-/+

▣ 입력예제 2 
3*(5+2)-9

▣ 출력예제 2
352+*9-

'''

a = input()
result = ''
operator = []

for x in a:
    if x.isdecimal():
        result += x
    else: # 연산자인 경우
        if x == '(':
            operator.append(x)
        elif x == '*' or x == '/':
            while operator and (operator[-1] == '*' or operator[-1] == '/'): # 우선순위가 같거나 낮으면 또는 여는 괄호가 아니면
                result += operator.pop()
            operator.append(x)
        elif x == '+' or x == '-':
            while operator and operator[-1] != '(': # 우선순위가 같거나 낮으면 또는 여는 괄호가 아니면
                result += operator.pop()
            operator.append(x)
        elif x == ')': # 닫는 괄호면 우선순위가 가장 낮으므로 원래 있던 걸 pop하는데 여는 괄호가 나올때 까지 pop해야함
            # 아래 나오는 while문과 같은 결과
            # while True:
            #     if operator[-1] != '(':
            #         result += operator.pop()
            #     else: # 여는 괄호도 제거
            #         operator.pop()
            #         break
            while operator and operator[-1] != '(': # 여는 괄호가 나올때 까지 pop해야함
                result += operator.pop()
            operator.pop() # '('를 없애기 위해

while operator:
    result += operator.pop()

print(result)
