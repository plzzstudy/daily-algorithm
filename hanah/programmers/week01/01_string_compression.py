# 문제 제목: 문자열 압축 (https://school.programmers.co.kr/courses/15414/lessons/132137)
# 문제 유형: 완전 탐색

def solution(s):
    min_len = 10000
    for slice_size in range(1, len(s)+1):
        start = 0
        end = slice_size
        a = []
        while True:
            if a and a[-1] == s[start:end]:
                a[-2] += 1
            else:
                a.append(1)
                a.append(s[start:end])

            start += slice_size
            end += slice_size

            if len(s[start:]) < slice_size:
                break
        
        # slice_size보다 길이가 작은 마지막 조각은 그냥 붙이기
        if s[start:]:
            a.append(s[start:])

        result = ''.join([str(x) for x in a if x != 1])

        if len(result) < min_len:
            min_len = len(result)

    return min_len