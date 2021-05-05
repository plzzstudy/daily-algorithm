```
# 대표값

N명의 학생의 수학점수가 주어집니다. 
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높 은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.
▣ 입력예제 1
10
45 73 66 87 92 67 75 79 75 80

▣ 출력예제 1
74 7
```



# solution1

N = int(input())
score = list(map(int, input().split()))

avg = round(sum(score) / len(score))
near_avg = [abs(avg-i) for i in score]
lowest = min(near_avg)
a = []
for j in range(len(near_avg)):
    if near_avg[j] == lowest:
        a.append(j)
b = 0
for k in a:
    if b < score[k]:
        b = score[k]
        result = k
print(avg, result+1)

#solution2

n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a) / n)
min=2147000000
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