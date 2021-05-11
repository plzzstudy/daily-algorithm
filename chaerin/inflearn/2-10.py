# 점수 계산

# 1번 문제가 맞는 경우 1점
# 앞의 문제에 대해서 답이 틀리다가 답이 맞는 처음 문제는 1점
# 연속으로 문제의 답이 맞는 경우
# 두 번째 문제는 2점, 세 번째 문제는 3점, ..., K 번째 문제는 K점

# 시험 문제의 채점 결과가 주어졌을 때,(1 : 답이 맞는 경우, 0 : 답이 틀린 경우)
# 총 점수를 계산하는 프로그램을 작성하시오.

N = int(input())
result = list(map(int, input().split()))

record = []
if result[0] == 1:
    record.append(1)
else:
    record.append(0)

for i in range(1, N):
    if result[i] == 1:
        if record[-1] != 0:
            record.append(record[-1]+1)
        else:
            record.append(1)
    else:
        record.append(0)
print(sum(record))


# solution
sum = 0
cnt = 0
for x in result:
    if x==1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)
