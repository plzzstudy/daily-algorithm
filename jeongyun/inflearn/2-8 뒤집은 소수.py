import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))


def reverse(x):
    return int(str(x)[::-1])


def isPrime(x):
    x = reverse(x)
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for i in a:
    if reverse(i) != 1 and isPrime(i):
        print(reverse(i))
