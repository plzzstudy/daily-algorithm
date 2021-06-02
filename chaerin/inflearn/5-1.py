# 가장 큰 수

# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다. 
# 여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)

n, m = map(int, input().split())

n=list(map(int, str(n)))
stack=[]
for x in n:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m!=0:
    stack=stack[:-m]
    
result=''.join(map(str, stack))
print(result)