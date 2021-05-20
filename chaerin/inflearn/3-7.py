# 사과나무

# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 
# 각 격자안에는 한 그루의 사과나무가 심어저 있다. 
# N의 크기는 항상 홀수이다. 
# 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때 
# 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.

N = int(input())
rec = [list(map(int, input().split())) for _ in range(N)]

apples = 0
a = N//2
b = N//2
for i in range(N):
    for j in range(a, b+1):
        apples += rec[i][j]
    if i < N//2:
        a -= 1
        b += 1
    else:
        a += 1
        b -= 1

print(apples)