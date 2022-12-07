## 내코드
def solution(n, k):
    a = 0
    b = 0
    while n > 1:
        if n % k == 0:
            b += 1
            n = n // k
        else:
            a += 1
            n -= 1

    return a + b


solution(17, 4)

## 모범코드
def solution(n, k):
    res = 0
    while True:
        target = (n // k) * k
        res += n - target
        n = target

        if n < k:
            break

        n //= k
        res += 1
    result += n - 1
    return result
