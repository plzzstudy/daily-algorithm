arr = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# solution1
for i in range(3):
    ch2 = []
    for j in range(7):
        # 가로
        ch1 = [arr[j][i+k] for k in range(5)]
        if ch1 == ch1[::-1]:
            cnt += 1

        # 세로
        ch2 = [arr[i+k][j] for k in range(5)]
        if ch2 == ch2[::-1]:
            cnt += 1

print(cnt)

# solution2
for i in range(3):
    for j in range(7):
        tmp = arr[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        
        # 세로 비교
        for k in range(2):
            if arr[i+k][j] != arr[i+5-k-1][j]:  # 5개에서 맨 첫번째꺼와 맨 마지막 비교, 2번째와 4번째 비교
                break
        else:
            cnt += 1
    
print(cnt)
