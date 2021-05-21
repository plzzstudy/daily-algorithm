# 격자판 회문수

# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 
# 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요. 
# 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        if a[i][j] == a[i][j+4] and a[i][j+1] == a[i][j+3]:
            cnt += 1
        if a[j][i] == a[j+4][i] and a[j+1][i] == a[j+3][i]:
            cnt += 1

print(cnt)


# solution
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1
print(cnt)