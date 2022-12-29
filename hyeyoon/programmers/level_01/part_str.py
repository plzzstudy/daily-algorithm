"""
https://school.programmers.co.kr/learn/courses/30/lessons/147355
크기가 작은 부분문자열
t	p	result
"3141592"	"271"	2
"500220839878"	"7"	8
"10203"	"15"	3
7//length =2  5
7  3  5 
12 - 7           6
"""


def solution(t, p):
    cnt = 0
    length = len(p)
    start = 0
    end = length
    for _ in range(len(t) - length + 1):
        spl = t[start:end]
        if int(spl) <= int(p):
            cnt += 1
        start += 1
        end += 1
    return cnt


solution("500220839878", "7")
