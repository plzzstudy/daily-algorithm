'''
# 알파코드 (DFS)

철수와 영희는 서로의 비밀편지를 암호화해서 서로 주고받기로 했다. 그래서 서로 어떻게 암 호화를 할 것인지 의논을 하고 있다.

영희 : 우리 알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당하여 번호로 보내기로 하자.

철수 : 정말 바보같은 생각이군!! 생각해 봐!!
만약 내가 “BEAN"을 너에게 보낸다면 그것을 암호화하면 25114이잖아!! 
그러면 이것을 다시 알파벳으로 복원할 때는 많은 방법이 존재하는데 어떻게 할건데... 
이것을 알파벳으로 바꾸면 BEAAD, YAAD, YAN, YKD 그리고 BEKD로 BEAN말고도 5가지나 더 있군.

당신은 위와 같은 영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데 얼마나 많은 방법인 있는지 구하세요.

▣ 입력설명
첫 번째 줄에 숫자로 암호화된 코드가 입력된다. 
(코드는 0으로 시작하지는 않는다, 코드의 길 이는 최대 50이다)
0이 입력되면 입력종료를 의미한다.

▣ 출력설명
입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력한다. 
그 가지 수도 출력한다. 단어의 출력은 사전순으로 출력한다.

▣ 입력예제 1 
25114

▣ 출력예제 1 
BEAAD
BEAN
BEKD
YAAD 
YAN 
YKD 
6

'''

import sys

# alpha = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
code = list(map(int, sys.stdin.readline().rstrip()))
n = len(code)
code.append(999)
cnt = 0

res = [0] * n

def dfs(L, res_index):
    global cnt, res
    if L == n:
        cnt += 1
        for i in range(res_index):  # for i in res로 하면 n번째 인덱스까지 차 있는 걸로 출력되므로 res_index까지만 출력하게 해야함
            # print(alpha[res[i]], end='') # 이게 더 빠름
            print(chr(res[i]+64), end='') # 같은 결과
        print()
    else:
        for i in range(1, 27):
            if code[L] == i: # 한자리수
                res[res_index] = i
                dfs(L+1, res_index+1)
            elif i >= 10 and int(str(code[L])+str(code[L+1])) == i:
                res[res_index] = i
                dfs(L+2, res_index+1)


dfs(0, 0)
print(cnt)


