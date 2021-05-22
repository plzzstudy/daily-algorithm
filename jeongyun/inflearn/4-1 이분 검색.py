import sys
# sys.stdin = open("input.txt", 'rt')
n, m = map(int, input().split())
a = list(map(int, input().split()))
# print(a)
a.sort()
# print(a)
lt = 0
rt = n-1
mid = (lt+rt) // 2
while lt <= rt:
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid - 1
        mid = (lt+rt) // 2
    elif a[mid] < m:
        lt = mid + 1
        mid = (lt+rt) // 2
