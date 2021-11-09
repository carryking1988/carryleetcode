# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.

# def sortColors(nums):
#     from collections import Counter
#
#     count = Counter(nums)
#     # Counter({2: 2, 0: 2, 1: 2})
#     for i in range(len(nums)):
#         if i < count[0]:
#             nums[i] = 0
#         elif i < count[0] + count[1]:
#             nums[i] = 1
#         else:
#             nums[i] = 2
#     return nums
#

def sortColors(nums):
    zero = 0
    two = len(nums) - 1
    i = 0
    while i <= two:
        if nums[i] == 0:
            nums[zero], nums[i] = nums[i], nums[zero]
            i += 1
            zero += 1
        elif nums[i] == 1:
            i += 1
        elif nums[i] == 2:
            nums[two], nums[i] = nums[i], nums[two]
            two -= 1
    return nums

nums = [2, 0, 2, 1, 1, 0]

print(sortColors(nums))
