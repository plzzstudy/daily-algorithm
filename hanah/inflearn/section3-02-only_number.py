'''
# 숫자만 추출
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉, 첫자리0은 자연수화 할 때 무시합니다. 

출력은120를출력하고, 다음줄에 120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

▣ 입력설명
첫 줄에 숫자가 섞인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.

▣ 출력설명
첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.

▣ 입력예제 1 
g0en2Ts8eSoft

▣ 출력예제 1 
28
6

'''
import math

string = input()

num = ""
for s in string:
    if s.isdecimal():
        num += s
num = int(num)
print(num)

cnt = 0
for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0 and i * i != num:
        cnt += 2
    elif i * i == num:
        cnt += 1
    
print(cnt)

# isdecimal은 0~9만 찾는다
# isdigit은 2의 제곱 과 같은 숫자의 형태도 찾는다.
