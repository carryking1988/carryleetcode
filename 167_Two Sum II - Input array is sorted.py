#  Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
#
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#

def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1
    while start < end:
        if numbers[start] + numbers[end] == target:
            return [start+1, end+1]
        elif numbers[start] + numbers[end] > target:
            end -= 1
        elif numbers[start] + numbers[end] < target:
            start += 1
        else:
            return None
    return [start+1, end+1]


# numbers = [2, 7, 11, 15]
# target = 9

# numbers = [2,3,4]
# target = 6
#
numbers = [-1,0]
target = -1

print(twoSum(numbers, target))
