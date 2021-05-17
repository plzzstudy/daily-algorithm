
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
