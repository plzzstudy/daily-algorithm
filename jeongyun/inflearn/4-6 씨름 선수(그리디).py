import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
player = []
for i in range(n):
    h, w = map(int, input().split())
    player.append((h, w))  # 튜플 형태로 넣음

player.sort()
player.reverse()

cnt = 0
heaviest = 0
for h1, w1 in player:
    if heaviest < w1:
        heaviest = w1
        cnt += 1

print(cnt)
