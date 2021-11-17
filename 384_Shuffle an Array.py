# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
import random


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        new_nums = self.nums[:]
        n = len(self.nums)
        for i in range(n):
            # temp_ran = random.randrange(i, n)
            # new_nums[i], new_nums[temp_ran] = new_nums[temp_ran], new_nums[i]
            temp = random.randrange(0, n - i)
            new_nums[temp], new_nums[n - i - 1] = new_nums[n - i - 1], new_nums[temp]

        return new_nums


nums = [i for i in range(1, 11)]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
