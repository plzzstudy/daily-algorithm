
# 문제 제목: 기능개발 (https://school.programmers.co.kr/courses/15414/lessons/132138)
# 문제 유형: Queue
from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while progresses:
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

    

    return answer