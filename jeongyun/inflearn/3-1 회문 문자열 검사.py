import sys
# sys.stdin = open("input.txt", "rt")
N = int(input())
for i in range(N):
    a = input()
    if a.lower() == a.lower()[::-1]:
        print(f'#{i+1}', 'YES')
    else:
        print(f'#{i+1}', 'NO')
