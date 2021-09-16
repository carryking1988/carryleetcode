# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.

def searchRange(nums, target):
    res = [-1, -1]
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left > right:
        return res







nums = [5, 7, 7, 8, 8, 10]
target = 6
print(searchRange(nums,target))


# def searchRange(nums, target):
# lo, hi = 0, len(nums) - 1
# while lo <= hi:
#     mid = (lo + hi) // 2
#     if nums[mid] == target:
#         break
#     elif nums[mid] > target:
#         hi = mid - 1
#     else:
#         lo = mid + 1
# if lo > hi:
#     return [-1, -1]
#
# midtarget = mid
#
# lo, hi = 0, mid
# leftpos = 0
# while lo <= hi:
#     if hi >= 1 and nums[hi - 1] != target or hi == 0:
#         leftpos = hi
#         break
#     mid = (lo + hi) // 2
#     if nums[mid] == target:
#         hi = mid
#     elif nums[mid] < target:
#         lo = mid + 1
#
# rightpos = 0
# lo, hi = midtarget, len(nums) - 1
#
# while lo <= hi:
#     if lo <= len(nums) - 2 and nums[lo + 1] != target or lo == len(nums) - 1:
#         rightpos = lo
#         break
#     mid = (lo + hi) // 2
#     if nums[mid] == target:
#         lo = mid
#     elif nums[mid] > target:
#         hi = mid - 1
# return [leftpos, rightpos]


# nums = [5, 7, 7, 8, 8, 10]
# target = 8
#
# nums = [2, 2]
# target = 2
# print(searchRange(nums, target))
