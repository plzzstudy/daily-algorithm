# solution1

N = int(input())
score = list(map(int, input().split()))

a = []
avg = round(sum(score) / len(score))

for i in range(len(score)):
    a.append(abs(avg-score[i]))
for j in range(len(a)):
    if a[j] <= a[j+1]:
        print(avg + j)
