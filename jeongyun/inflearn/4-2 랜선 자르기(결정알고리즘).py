import sys
# sys.stdin = open("input.txt", 'rt')


def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt  # 그 길이로 만들 수 있는 랜선 개수가 나옴


k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) >= n:
        res = mid
        # 더 좋은 답을 찾아서 더 긴 길이로 가야돼
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
