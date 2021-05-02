from itertools import combinations

# solution1(내가 쓴 코드)
n, k = map(int, input().split())
list_num = list(map(int, input().split()))
list_sum = [sum(nums) for nums in combinations(list_num, 3)]
set_sum = sorted(set(list_sum), reverse=True)

print(set_sum[k-1])


# solution2
result = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for m in range(j+1, n):
            result.add(list_num[i] + list_num[j] + list_num[m])

result = sorted(result, reverse=True)
print(result[k-1])
