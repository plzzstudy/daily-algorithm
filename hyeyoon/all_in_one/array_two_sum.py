# a = list(map(int, input().split()))
# print(a)

# O(n^2)
# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n - 1):
#         for j in range(i + 1, n - 1):
#             if nums[i] + nums[j] == target:
#                 return True
#     return False


# print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))

# Onlogn
def twoSum(nums, target):
    nums.sort()  # -> O(nlongn)
    l, r = 0, len(nums) - 1
    while l < r:
        # O(n)
        if nums[l] + nums[r] == target:
            return True
        elif nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
    return False


print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))
