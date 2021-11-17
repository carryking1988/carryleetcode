# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# You may assume the input array always has a valid answer.
def wiggleSort(nums):
    nums.sort()
    mid = (len(nums) + 1) // 2
    left, right = nums[:mid], nums[mid:]
    nums[::2] = left[::-1]
    nums[1::2] = right[::-1]

nums = [1,3,2,2,3,1]
wiggleSort(nums)
print(nums)
