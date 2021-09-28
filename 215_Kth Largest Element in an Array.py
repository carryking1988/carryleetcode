# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# use bubblesort to find out the kth element of the array
# def findKthLargest(nums, k):
#     if k <= len(nums):
#         for i in range(len(nums)):
#             for j in range(len(nums)-i-1):
#                 if nums[j] < nums[j + 1]:
#                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     return nums[k - 1]


# 使用选择排序selectionSort
# def findKthLargest(nums, k):
#     if k <= len(nums):
#         for i in range(k):
#             max_idx = i
#             for j in range(i+1, len(nums)):
#                 if nums[max_idx] < nums[j]:
#                     max_idx = j
#             nums[i], nums[max_idx] = nums[max_idx], nums[i]
#     # print(nums)
#         return nums[k - 1]


# nums = [3, 2, 1, 5, 6, 4]
# k = 2

# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4


# print(findKthLargest(nums, k))


def findKthLargest(nums, k):
    left, right = 0, len(nums) - 1
    target = len(nums) - k
    while left < right:
        mid = quickSelection(nums, left, right)
        if mid == target:
            return nums[mid]
        if mid < target:
            left = mid + 1
        else:
            right = mid - 1
    return nums[left]


def quickSelection(nums, left, right):
    i = left + 1
    j = right
    while True:
        while i < right and nums[i] <= nums[right]:
            i += 1
        while left < j and nums[j] >= nums[left]:
            j -= 1

        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[j] = nums[j], nums[left]
    return j


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 1
print(quickSelection(nums, 0, len(nums) - 1))
