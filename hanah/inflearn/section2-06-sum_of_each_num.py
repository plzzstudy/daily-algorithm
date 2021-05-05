'''
# 자릿수의 합

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요. 
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를 출력합니다.

▣ 입력예제 1 
3
125 15232 97

▣ 출력예제 1 
97

'''

n = int(input())
nums = list(map(int, input().split()))


# solution1
def digit_sum(x):
    sum = 0
    for n in str(x):
        sum += int(n)

    return sum


# solution2
def digit_sum2(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10

    return sum


max_sum = 0
for num in nums:
    if digit_sum(num) > max_sum:
        max_sum = digit_sum(num)
        result = num

print(result)
