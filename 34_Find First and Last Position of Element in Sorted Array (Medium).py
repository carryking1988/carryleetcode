# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.

def searchRange(nums, target):
    res = [-1, -1]
    left, right = 0, len(nums) - 1
    # left
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if mid == 0 or mid > 0 and nums[mid - 1] != target:
                res[0] = mid
                break
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    # right
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or mid < len(nums) - 1 and nums[mid + 1] != target:
                res[1] = mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return res


nums = [1, 1, 2, 2, 3, 3, 3, 5, 5, 5, 6, 7, 8, 8, 9]
target = 8

print(searchRange(nums, target))
