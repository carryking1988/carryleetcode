"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


# def merge(num1, m, num2, n):
#     left = m - 1
#     right = n - 1
#     while left >= 0 and right >= 0:
#         if num1[left] <= num2[right]:
#             num1[left + right + 1] = num2[right]
#             right -= 1
#         else:
#             num1[left + right + 1], num1[left] = num1[left], num1[left + right + 1]
#             left -= 1


def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    nums1[:n] = nums2[:n]


# def merge2(nums1, m, nums2, n):
#     # nums = [n1 for i, n1 in enumerate(nums1) if i < m] +[n2 for j,n2 in enumerate(nums2) if j < n]
#     nums = nums1[:m]+nums2[:n]
#     nums.sort()
#     for i,num in enumerate(nums):
#         nums1[i] = num


# merge(num1=[1, 2, 3, 0, 0, 0], m=3, num2=[2, 5, 6], n=3)

num1 = [4, 9, 12, 0, 0, 0]
m = 3
num2 = [3, 10, 16]
n = 3
merge(num1, m, num2, n)
print(num1)
