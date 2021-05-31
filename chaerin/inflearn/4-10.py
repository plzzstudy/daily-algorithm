# 역수열(그리디)

# 1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때,
# 1부터 n까지 각각의 수 앞에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.
# 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 
# 원래의 수열을 출력하는 프로그램을 작성하세요.

n=int(input())
a=list(map(int, input().split()))

result=[0]*n
cnt=0
for i in range(n):
    for j in range(n):
        if a[i]==0 and result[j]==0:
            result[j]=i+1
            break
        elif result[j]==0:
            a[i]-=1
for x in result:
    print(x, end=' ')