# 랜선자르기

# 길이가 제각각인 K개의 랜선을 모두 길이가 같은 N개의 랜선으로 만들려고 한다.
# 이미 자른 랜선은 붙일 수 없다.
# 그 외에 손실되는 길이는 없다고 가정하며, 
# 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정한다.
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
# 이 때 만들수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

def Count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

k, n = map(int, input().split())
line = []
result = 0
largest = 0
for _ in range(k):
    a = int(input())
    line.append(a)
    largest = max(largest, a)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(result)