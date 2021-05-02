# K번째 큰 수

# 1부터 100까지의 자연수가 적힌 N장의 카드 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 구한다.
# 이 때, 더한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하세요.

N, K = map(int, input().split())
a = list(map(int, input().split()))

sum = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum.add(a[i] + a[j] + a[k])

sum = list(sum)
sum.sort()
print(sum[-K])