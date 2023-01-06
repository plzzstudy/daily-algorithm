'''
https://school.programmers.co.kr/learn/courses/30/lessons/133499?language=python3
옹알이 2
babbling	result
["aya", "yee", "u", "maa"]	1
["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	2
'''
# 55점
def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    answer = 0
    for bab in babbling:
        for i in can:
            bab = bab.replace(i, '',1)
        if len(bab) == 0:
            answer+=1
    return answer


solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])


# 반복 되는걸 *2로 처리
def solution1(babbling):
    can = ["aya", "ye", "woo", "ma"]
    answer = 0
    for bab in babbling:
        for i in can:
            if i*2 not in bab:
                bab = bab.replace( i, ' ')
        if len(bab.strip()) == 0:
            answer+=1
    return answer

solution1(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])