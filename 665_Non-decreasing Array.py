# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).


def checkPossibility(nums):
    if len(nums) == 0:
        return False
    amount = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if i == 0:
                nums[0] = nums[1]
            elif nums[i-1] > nums[i+1]:
                nums[i+1] = nums[i]
            elif nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            amount += 1
            print(nums)
        if amount > 1:
            return False
    return True

# nums = [4,2,3]
# nums = [4,2,1]
# nums = [3, 4, 2, 3]
# nums = [3, 5, 1, 2, 3]
# nums = [3, 4, 2, 6, 8]
nums = [1,4,1,2]
print(checkPossibility(nums))
