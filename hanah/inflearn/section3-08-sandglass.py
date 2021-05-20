'''
# 곳감(모래시계)

현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 
현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.

그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.

첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회 전하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.


▣ 입력설명
첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다. 
그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령 정보가 M줄에 걸쳐 주어집니다.

▣ 출력설명
총 감의 개수를 출력합니다.

▣ 입력예제 1
5
10 13 10 12 15
12 39 39 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3 
2 0 3 
5 1 2 
3 1 4

▣ 출력예제 1 
362

'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# solution1
for _ in range(m):
    r, d, x = map(int, input().split())
    new = [0] * n
    if d == 0:
        x *= (-1)
    
    for i in range(n):
        ny = i + x
        if ny < 0:
            ny += n
        elif ny >= n:
            ny -= n

        new[ny] = arr[r-1][i]
    arr[r-1] = new


# solution2
for _ in range(m):
    r, d, x = map(int, input().split())
    
    if d == 0:
        for _ in range(x):
            a = arr[r-1].pop(0) # pop을 하면 지정한 인덱스의 요소가 빠지고 하나씩 땡겨짐
            arr[r-1].append(a)
    else:
        for _ in range(x):
            a = arr[r-1].pop()
            arr[r-1].insert(0, a)
    

s, e = 0, n-1
result = 0
for i in range(n):
    for j in range(s, e+1):
        result += arr[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(result)

