"""
다트 게임
https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""


def solution(dartResult):
    stack = []
    a = {"S": 1, "D": 2, "T": 3}
    dartResult = dartResult.replace("10", "X")
    for i in dartResult:
        if i.isdigit() or i == "X":
            stack.append(int(i) if i != "X" else 10)
        elif i in ("S", "D", "T"):
            print(i, stack)
            num = stack.pop()
            stack.append(num ** a[i])
        elif i == "#":
            stack[-1] *= -1
        elif i == "*":
            if len(stack) > 1:
                stack[-1] *= 2
                stack[-2] *= 2
            else:
                stack[-1] *= 2
    return sum(stack)
