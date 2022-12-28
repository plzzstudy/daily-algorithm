"""
https://school.programmers.co.kr/learn/courses/30/lessons/138477
명예의 전당 (1)

3	[10, 100, 20, 150, 1, 100, 200]
일자별로 for문 돌면서 
res = sorting
"""


def solution(k, score):
    res = []
    answer = []
    for i in score:
        res.sort()
        if len(res) < k:
            res.append(i)

        elif len(res) == k and res[0] < i:
            res[0] = i
        answer.append(min(res))
    return answer


solution(3, [10, 100, 20, 150, 1, 100, 200])
