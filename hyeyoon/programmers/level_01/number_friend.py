"""
https://school.programmers.co.kr/learn/courses/30/lessons/131128
숫자짝꿍
"""

# 이렇게 하면 73점.. 4문제 시간 초과 ...
def solution1(X, Y):
    x = list(X)
    y = list(Y)
    answer = ""
    res = ""
    for i in x:
        if i in y:
            y.remove(i)
            answer += i
    if answer == "":
        res = "-1"
    elif int(answer) > 0:
        res = "".join(sorted(answer, reverse=True))
    else:
        res = "0"
    return res


# 합계: 73.7 / 100.0
def solution(X, Y):
    answer = ""
    for i in range(9, -1, -1):
        x_c = min(X.count(str(i)), Y.count(str(i)))
        if x_c >= 0:
            for _ in range(x_c):
                answer += str(i)
    if answer == "":
        return "-1"
    elif int(answer) > 0:
        return "".join(answer, reverse=True)
    else:
        return "0"


solution("100", "2345")

# 0에 대한 처리에서 시간초과난듯.
# 100점 코드..
def solution(X, Y):
    answer = ""
    for i in range(10):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))
    if answer == "":
        return "-1"
    elif len(answer) == answer.count("0"):
        return "0"
    else:
        return "".join(sorted(answer, reverse=True))
