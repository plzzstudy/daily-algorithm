'''
#스토쿠 검사

스도쿠는 매우 간단한 숫자 퍼즐이다. 
9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9 개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 

각 행에 1부터 9까지의 숫자가 중복 없이 나오 고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색 깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.

▣ 출력설명
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

▣ 입력예제 1 
143628579 
572139468 
986754231 
391542786 
468917352 
725863914 
237481695 
619275843 
854396127
▣ 출력예제 1 
YES
'''

# solution
def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")