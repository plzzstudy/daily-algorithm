import sys
sys.stdin = open("input.txt", 'rt')


def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt  # 필요한 DVD의 개수


n, m = map(int, input().split())
Music = list(map(int, input().split()))
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) <= m:
        res = mid
        rt = mid - 1  # 더 좋은 답을 찾아야 됨
    else:  # DVD 용량이 너무 작은 경우
        lt = mid + 1
print(res)
