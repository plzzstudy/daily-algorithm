'''
# 가장 큰 수

선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다.
단, 숫자의 순서는 유지해야 합니다.

만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.

▣ 입력설명
첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.

▣ 출력설명
가장 큰 수를 출력합니다.

▣ 입력예제 1 
5276823 3

▣ 출력예제 1 
7823

▣ 입력예제 2 
9977252641 5

▣ 출력예제 2 
99776

'''
n, m = map(int, input().split())

# solution1
str_n = str(n)
len_n = len(str_n)

res = [str_n[0]]
cnt = 0
for i in range(1, len_n):
    while res and cnt < m and str_n[i] > res[-1]: # res맨 끝 수보다 크면 res맨 끝 숫자를 삭제하고 자기자신 집어넣기
        res.pop()
        cnt += 1
    res.append(str_n[i])

# m만큼 제거를 다 못한 경우
if len(res) > len_n - m:
    x = len(res) - (len_n-m)
    res = res[:-x] # res는 이미 내림차순으로 되어있기 때문에 뒤에 남은 카운드만큼만 제거

print(''.join(res))

# solution2
num = list(map(int, str(n)))
stack = []

for x in num:
    while stack and m > 0 and x > stack[-1]:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

print(''.join(map(str, stack)))

