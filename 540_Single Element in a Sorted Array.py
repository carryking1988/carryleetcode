# You are given a sorted array consisting of only integers where every element appears exactly twice,
#
# except for one element which appears exactly once. Find this single element that appears only once.
#
# Follow up: Your solution should run in O(log n) time and O(1) space.

def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == nums[mid - 1]:
            if (left + mid - 1) % 2 == 0:
                left = mid + 1
            else:
                right = mid - 2
        elif nums[mid] == nums[mid + 1]:
            if (left + mid) % 2 == 0:
                left = mid + 2
            else:
                right = mid - 1
        else:
            return nums[mid]
    return nums[left]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2
print(singleNonDuplicate(nums))

nums = [3, 3, 7, 7, 8, 8, 10, 11, 11]
# Output: 10
print(singleNonDuplicate(nums))
