'''
# 회문 문자열:

N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 
회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.

단, 회문을 검사할 때 대소문자를 구분하지 않습니다.


▣ 입력설명
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.

▣ 출력설명
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

▣ 입력예제 1 
5
level
moon
abcba 
soon 
gooG

▣ 출력예제 1 
#1 YES
#2 NO
#3 YES
#4 NO 
#5 YES

'''

# solution1

n = int(input())

for i in range(1, n+1):
    str = input().lower()
    size = len(str)
    for j in range(size//2):
        if str[j] != str[-(j+1)]:
            print(f'#{i} NO')
            break
    else:
        print(f'#{i} YES')


# solution2

for i in range(1, n+1):
    str = input().lower()
    if str == str[::-1]:
        print(f'#{i} YES')
    else:
        print(f'#{i} NO')

