# 내 답
n = int(input())
plan = list(map(str, input().split()))
current = [1, 1]
# L U R D
d = {"L": [0, -1], "U": [1, 0], "R": [0, 1], "D": [-1, 0]}
for i in plan:
    if (
        current[0] + d[i][0] >= 0
        and current[1] + d[i][1] >= 0
        and current[0] + d[i][0] <= n
        and current[1] + d[i][1] <= n
    ):
        current[0] += d[i][0]
        current[1] += d[i][1]
print(current[0], current[1])

# 모범 답안
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dx[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
