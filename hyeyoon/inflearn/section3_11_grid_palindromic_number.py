'''
#격자판 회문수
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요. 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

▣ 입력설명
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.

▣ 출력설명 
5자리 회문수의 개수를 출력합니다.
▣ 입력예제 1 
2415326 3518717 8327138 6123211 1313532 1125652 1222215
▣ 출력예제 1 
3

'''

#solution1
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)



#solution2
<회문의 길이가 가변적일 때 코드>

board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
len=5
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+len]
        if tmp==tmp[::-1]:
            cnt+=1
        #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
        for k in range(len//2):
            if board[i+k][j]!=board[len-k+i-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)


