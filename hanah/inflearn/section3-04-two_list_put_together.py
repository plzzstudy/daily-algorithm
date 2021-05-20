'''
# 두 리스트 합치기

오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.

▣ 입력예제 1 
3
1 3 5
5
2 3 6 7 9

▣ 출력예제 1 
1 2 3 3 5 6 7 9
'''

n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))

# c = a+b
# c.sort()

# for x in c:
#     print(x, end=" ")

# sort()를 사용하면 O(NlogN)인데 문제에서 두 리스트가 이미 오름차순으로 정렬되어있다는 것을 이용하면 O(N)으로 문제를 풀 수 있다.

# >> two point 활용하여 O(N)
p1 = p2 = 0
result = []

while p1 < n1 and p2 < n2:
    if a[p1] < b[p2]:
        result.append(a[p1])
        p1 += 1
    else:
        result.append(b[p2])
        p2 += 1

if p1 == n1:
    result += b[p2:]

if p2 == n2:
    result += a[p1:]

for x in result:
    print(x, end=" ")
