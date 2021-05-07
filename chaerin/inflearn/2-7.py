# 소수(에라토스테네스 체)

# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.

# 20이 입력되면 1부터 20까지의 소수는
# 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.

N = int(input())

sieve = [True] * (N+1)
cnt = 0
for i in range(2, N+1):
    if sieve[i] == True:
        cnt += 1
        for j in range(i, N+1, i):
            sieve[j] = False
print(cnt)