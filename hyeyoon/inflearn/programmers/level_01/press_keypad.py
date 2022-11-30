"""
https://school.programmers.co.kr/learn/courses/30/lessons/67256
"""


def solution(numbers, hand):
    answer = ""
    dict_ = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
        "*": [3, 0],
        "#": [3, 2],
    }
    left_now = dict_["*"]
    right_now = dict_["#"]
    for i in numbers:
        now = dict_[i]
        if i in [1, 4, 7]:
            answer += "L"
            left_now = now
        elif i in [3, 6, 9]:
            answer += "R"
            right_now = now
        else:
            right = abs(now[0] - right_now[0]) + abs(now[1] - right_now[1])
            left = abs(now[0] - left_now[0]) + abs(now[1] - left_now[1])
            if right < left:
                answer += "R"
                right_now = now
            elif left < right:
                answer += "L"
                left_now = now
            else:
                if hand == "right":
                    answer += "R"
                    right_now = now
                else:
                    answer += "L"
                    left_now = now
    return answer


solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
