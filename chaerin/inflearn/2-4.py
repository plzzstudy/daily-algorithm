# 대표값

# N명의 학생의 수학점수가 주어집니다.
# N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.

# 답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요.
# 답이 되는 점수가 두개일 경우 번호가 빠른 학생의 번호를 답으로 합니다.

import math

N = int(input())
score = list(map(int, input().split()))
average = round(sum(score)/len(score))

close = score[0]
for i in score[1:]:
    if abs(i-average) < abs(close-average):
        close = i
    elif abs(i-average) == abs(close-average):
        if i > close:
            close = i

print(average, score.index(close)+1)



# solution
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)