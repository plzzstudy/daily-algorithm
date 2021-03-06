'''
# 소수 (에라토스테네스의 체)

자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 
제한시간은 1초입니다.

▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.

▣ 입력예제 1 
20

▣ 출력예제 1 
8

'''

# N이하의 수 중에서 모든 소수를 구하는 문제는 시간복잡도 상 '에라토스테네스의 체' 알고리즘을 활용하는 것이 가장 빠르다.

# solution1
import math

n   = int(input())
arr = [True] * (n+1)

arr[0], arr[1] = False, False

for i in range(2, int(math.sqrt(n)) + 1): # n의 제곱근 수 까지만 탐색
    j = 2
    while i * j <= n:
        arr[i * j] = False
        j += 1

print(arr.count(True))

# solution2
ch  = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)
