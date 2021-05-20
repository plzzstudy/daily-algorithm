'''
# 스도쿠 검사

각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고,
각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오면 스도쿠를 정확하게 푼 것이다.
완성된 9×9 크기의 스도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.


'''

arr = [list(map(int, input().split())) for _ in range(9)]
nums = list(range(1, 10))

# solution1
def check_rc():
    for i in range(9):
        if sorted(arr[i]) != nums:
            return False

        check = [arr[j][i] for j in range(9)]
        if sorted(check) != nums:
            return False

    return True

def check_3():
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            check = [arr[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if sorted(check) != nums:
                return False
    return True


if check_rc() and check_3():
    print("YES")
else:
    print("NO")


# solution2 
def check():
    for i in range(9):
        ch1 = ch2 = [0]*10
        for j in range(9):
            ch1[arr[i][j]] = 1
            ch2[arr[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[arr[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    
    return True

if check():
    print("YES")
else:
    print("NO")
