```
#소수
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 
제한시간은 1초입니다.

▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.

▣ 입력예제 1 20

▣ 출력예제 1 8

```
# solution1 ==>시간 초과
n = int(input())
a = []

for i in range(2, n):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        a.append(i)
print(len(a))

# solution2 ==> 에라토스테네스 체
n = int(input())
ch = [0] * (n+1)
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)