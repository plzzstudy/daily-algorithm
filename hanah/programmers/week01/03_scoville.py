# 문제 제목: 더 맵게 (https://school.programmers.co.kr/courses/15414/lessons/132140)
# 문제 유형: 우선순위 큐
from heapq import heapify, heappush, heappop

def _mix(min_1, min_2):
    return min_1 + (min_2 * 2)

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) >= 2:
            min_1 = heappop(scoville)
            min_2 = heappop(scoville)
            mixed = _mix(min_1, min_2)
            heappush(scoville, mixed)
            cnt += 1
        else:
            return -1  # K보다 작은 값이 남아있는데 인덱스가 부족한 경우 >> 더이상 계산을 할 수 없으므로 이 케이스는 끝. 

    if cnt == 0:
        return -1
    return cnt
