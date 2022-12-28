"""
https://school.programmers.co.kr/learn/courses/30/lessons/136798
"""

# 합계: 66.7 / 100.00 -> 시간초과
def solution(number, limit, power):
    res = {}
    answer = 0
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                try:
                    res[i] += 1
                except:
                    res[i] = 1
    for q in res.values():
        if q > limit:
            answer += power
        else:
            answer += q
    # print(answer)
    return answer


solution(5, 3, 2)

##성공 코드
def solution1(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                if j == i // j:
                    cnt += 1
                else:
                    cnt += 2
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer


solution1(5, 3, 2)
