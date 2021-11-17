# Given an array of integers nums, you start with an initial positive value startValue.
#
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.


def minStartValue(nums):
    res = 1
    pre = 1
    for i in nums:
        if i + pre < 1:
            res += 1 - (i + pre)
            pre = 1
        else:
            pre += i
    return res
nums1 = [-3, 2, -3, 4, 2]

nums2 = [1, -2, -3]

nums3 = [1, 2]

nums4 = [-5, -2, 4, 4, -2]

print(minStartValue(nums1))
print(minStartValue(nums2))
print(minStartValue(nums3))
print(minStartValue(nums4))
