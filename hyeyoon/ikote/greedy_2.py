"""
곱하기 또는 더하기 
"""
## 내코드
def solution(n):
    start = int(n[0])
    for i in range(1, n + 1):
        if n[i] <= 1 or start <= 1:
            start += n[i]
        else:
            start *= n[i]

    return start


"""
모험가 길드
"""

### 모범 답안
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0
count = 0
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
