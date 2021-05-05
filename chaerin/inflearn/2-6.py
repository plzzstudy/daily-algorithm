# 자릿수의 합

# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
# 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.

# 각 자연수의 자릿수의 합을 구하는 함수를
# def digit_sum(x)를 작성하여 프로그래밍 하세요.

N = int(input())
nums = map(int, input().split())

def digit_sum(x):
    a = 0
    for i in str(x):
        a += int(i)
    return a

max_sum = 0
result = 0
for num in nums:
    if max_sum < digit_sum(num):
        max_sum = digit_sum(num)
        result = num
print(result)