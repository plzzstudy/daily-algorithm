import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
ch = [0] * (n+1)  # n+1 로 해야 인덱스 번호가 n까지 생김
cnt = 0  # cnt는 소수의 개수
for i in range(2, n+1):  # n까지 돌아야 되니까 n+1
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):  # i의 배수로 반복
            ch[j] = 1
print(cnt)
