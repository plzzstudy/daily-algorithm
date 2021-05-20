# 주사위 게임

# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서
# 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

# 규칙(1) 같은 눈이 3개가 나오면 10,000원 + (같은 눈) * 1,000원의 상금을 받게 된다.
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원 + (같은 눈) * 100원의 상금을 받게 된다.
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈) * 100원의 상금을 받게 된다.

# N명이 주사위 게임에 참여하였을 때,
# 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을 작성하시오.

N = int(input())

result = 0
for i in range(N):
    eyes = input().split()
    eyes.sort()
    a, b, c = map(int, eyes)
    if a==b and b==c:
        money = 10000 + a * 1000
    elif a==b or a==c:
        money = 1000 + (a * 100)
    elif b==c:
        money = 1000 + (b * 100)
    else:
        money = c * 100
    if money > result:
        result = money

print(result)
