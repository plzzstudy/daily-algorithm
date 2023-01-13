'''
문자열 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/140108
s	result
"banana"	3
"abracadabra"	6
"aaabbaccccabba"	3
'''

def solution(s):
    x_cnt = 0
    n_cnt = 0
    answer = 0
    x = s[0]
    for i in range(len(s)):
        if s[i] == x:
            x_cnt+=1
        else:
            n_cnt+=1
        if x_cnt == n_cnt or i == len(s)-1:
            answer+=1
            if i < len(s)-1:
                x = s[i+1]
            x_cnt=0
            n_cnt=0 
    return answer

solution("abracadabra")