import sys
sys.stdin = open("input.txt", "rt")
a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        ch1 = []
        ch2 = []
        for k in range(j, j+5):
            ch1.append(a[i][k])
            ch2.append(a[k][i])
        if ch1 == ch1[::-1]:
            cnt += 1
        if ch2 == ch2[::-1]:
            cnt += 1
        # print('ch1:', ch1)
        # print('ch2:', ch2)
print(cnt)
