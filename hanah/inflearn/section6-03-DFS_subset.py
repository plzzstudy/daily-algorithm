'''
# 부분집합 구하기(DFS)

자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.

▣ 출력설명
첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력예제와 같은 순서로 출력한다. 단 공집합은 출력하지 않습니다.

▣ 입력예제 1 
3

▣ 출력예제 1 
1 2 3
1 2
1 3
1 2
3 2
3

'''

# solution1 (combinations)  >> 이렇게 풀면 출력 순서 때문에 오답처리됨. 
#from itertools import combinations
#
#n = int(input())
#nums = [i for i in range(1, n+1)]
#res = []
#
#for i in range(1, n+1):
#    res.extend(combinations(nums, i))
#
#for x in res: # x는 튜플형
#    for n in x:
#        print(n, end=' ')
#    print()


# solution2 (DFS)
def dfs(x):
    if x == (n + 1):
        # check 값이 1인것만 출력
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
    else:
        check[x] = 1 # x가 부분집합에 사용 되었을 때의 경우
        dfs(x + 1)

        check[x] = 0 # x가 부분집합에 사용 되었을 때의 경우
        dfs(x + 1)
        
n = int(input())
check = [0] * (n+1) # 인덱스에 해당하는 수가 부분집합에 포함된 경우는 1, 포함되지 않은 경우는 0
dfs(1)
    
