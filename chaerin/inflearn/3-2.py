# 숫자만 추출

# 문자와 숫자가 섞여 있는 문자열이 주어지면
# 그 중 숫자만 추출하여 그 순서대로 자연수를 만든다.
# 만들어진 자연수와 그 자연수의 약수 개수를 출력한다.

a = input()

number = ''
for i in a:
    for j in range(10):
        if i == str(j):
            number+=i

number = int(number)
divisor = 0
for i in range(1, number+1):
    if number % i == 0:
        divisor += 1

print(number)
print(divisor)


# solution
res = 0
for i in a:
    if i.isdecimal():
        res = res*10+int(i)
print(res)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)


