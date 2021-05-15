N, M = map(int, input().split())
A = list(map(int, input().split()))
lt = 0
rt = 1
tot = A[0]
cnt = 0

# Time Limit Error 발생
for a in range(N):
    sum = A[a]
    if sum == M:
        cnt += 1
    for b in range(a+1, N):
        sum += A[b]
        if sum == M:
            cnt += 1
print(cnt)


# solution
while True:
    if tot < M:
        if rt < N:
            tot += A[rt]
            rt += 1
        else:
            break
    elif tot == M:
        cnt += 1
        tot -= A[lt]
        lt += 1
    else:
        tot -= A[lt]
        lt += 1
print(cnt)