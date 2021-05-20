# 뒤집은 소수

# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 
# 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요.

# ex) 
# 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력.
# 910을 뒤집으면 19로 숫자화 해야한다. 첫 자리부터의 연속된 0은 무시한다.

# 뒤집는 함수인 def reverse(x)와 
# 소수인지를 확인하는 함수 def ifPrime(x)를 반드시 작성하여 프로그래밍 한다.

N = int(input())
numbers = list(map(int, input().split()))

def reverse(x):
    rev_num = ''
    for i in str(x):
        rev_num = i + rev_num
    return int(rev_num)

def ifPrime(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    return False

for number in numbers:
    if ifPrime(reverse(number)) == True:
        print(reverse(number), end=' ')