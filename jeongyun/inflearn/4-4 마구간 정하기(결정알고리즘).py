import sys
# sys.stdin = open("input.txt", 'rt')


def Count(distance):
    before = a[0]
    cnt = 1
    for i in range(1, n):
        if (a[i] - before) >= distance:
            cnt += 1
            before = a[i]
    return cnt  # 배치할 수 있는 말의 수


n, c = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
# print(a)
lt = min(a)
rt = max(a)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1  # 더 좋은 답을 찾아야 됨
    else:  # 거리가 너무 큰 경우
        rt = mid - 1
print(res)
