# 스도쿠 검사

# 완성된 9×9 크기의 수도쿠가 주어지면 
# 정확하게 풀었으면 “YES", 
# 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.

def check(a):
    for i in range(9):
        x = [0] * 10
        y = [0] * 10
        for j in range(9):
            x[a[i][j]] = 1
            y[a[j][i]] = 1
        if sum(x) != 9 or sum(y) != 9:
            return False
    for i in range(3):
        for j in range(3):
            z = [0] * 10
            for k in range(3):
                for s in range(3):
                    z[a[i*3+k][j*3+s]] = 1
            if sum(z) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print('YES')
else:
    print('NO')