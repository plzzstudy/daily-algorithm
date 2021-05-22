'''
# 역수열(그리디)

1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 1부터 n까지 각각의 수 앞 에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.

예를 들어 다음과 같은 수열의 경우

    4 8 6 2 5 1 3 7

1앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5. 이렇게 5개이고,
2앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,
3앞에 놓인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개......

따라서 4 8 6 2 5 1 3 7의 역수열은 5 3 4 0 2 1 1 0 이 된다.

n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원래의 수열을 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<100)이 주어지고, 두 번째 줄에는 역수열이 숫자 사이에 한
칸의 공백을 두고 주어진다.

▣ 출력설명 
원래 수열을 출력합니다.


▣ 입력예제 1
8
5 3 4 0 2 1 1 0

▣ 출력예제 1 
4 8 6 2 5 1 3 7
'''

n = int(input())
a = list(map(int, input().split()))

# solution1
a.reverse()
result = [n]
for i in range(1, n):
    result.insert(a[i], n-i)

for x in result:
    print(x, end=' ')

# solution2
result = [0] * n
for i in range(n):
    for j in range(n):
        if a[i] == 0 and result[j] == 0: # result가 0인 지점에 i + 1 값으로 채운다
            result[j] = i + 1
            break # 자리를 찾아 주었기 때문에 다음 i로 넘어감
        elif result[j] == 0: # a[i]가 0이 될 때 까지 j를 증가시킴
            a[i] -= 1
        # result[j]가 0이 아닌 경우는 그냥 j만 증가시키면 됨 

for x in result:
    print(x, end=' ')

